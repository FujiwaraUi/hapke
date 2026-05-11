#!/usr/bin/env python3
"""search.py — Hybrid 検索 + LLM 回答生成

ChromaDB（ベクトル検索）と BM25（キーワード検索）を Reciprocal Rank Fusion で
統合し、Qwen2.5-7B で回答を生成する CLI ツール。

使い方:
  .venv/bin/python3 hapke_rag/search.py --query "双方向反射率の定義"
  .venv/bin/python3 hapke_rag/search.py --query "equation (8.12)"
  .venv/bin/python3 hapke_rag/search.py --query "single-scattering albedo" --no-llm
"""

from __future__ import annotations

import argparse
import json
import pickle
import sys
from pathlib import Path

import chromadb
import requests
from rank_bm25 import BM25Okapi


# ---------------------------------------------------------------------------
# 設定
# ---------------------------------------------------------------------------

OLLAMA_BASE_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "qwen2.5:7b"
COLLECTION_NAME = "hapke_rag"

TOP_K_VECTOR = 10
TOP_K_BM25 = 10
TOP_K_FINAL = 5
RRF_K = 60  # Reciprocal Rank Fusion の定数


# ---------------------------------------------------------------------------
# Ollama API
# ---------------------------------------------------------------------------

def check_ollama() -> bool:
    try:
        r = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        return r.status_code == 200
    except requests.ConnectionError:
        return False


def ollama_embed(texts: list[str]) -> list[list[float]]:
    """テキストを embedding に変換する。"""
    resp = requests.post(
        f"{OLLAMA_BASE_URL}/api/embed",
        json={"model": EMBED_MODEL, "input": texts},
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["embeddings"]


def ollama_generate(prompt: str, system: str = "") -> str:
    """Qwen2.5 でテキストを生成する。"""
    payload: dict = {
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.3, "num_predict": 1024},
    }
    if system:
        payload["system"] = system

    resp = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json=payload,
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()["response"]


# ---------------------------------------------------------------------------
# 日本語判定 + 英訳
# ---------------------------------------------------------------------------

def _is_japanese(text: str) -> bool:
    """テキストに日本語文字が含まれるか判定する。"""
    for ch in text:
        cp = ord(ch)
        # ひらがな、カタカナ、CJK統合漢字
        if (0x3040 <= cp <= 0x309F
                or 0x30A0 <= cp <= 0x30FF
                or 0x4E00 <= cp <= 0x9FFF):
            return True
    return False


def translate_to_english(query: str) -> str:
    """日本語クエリを英語に翻訳する。"""
    prompt = (
        "Translate the following Japanese text to English. "
        "Output only the translation, nothing else.\n\n"
        f"{query}"
    )
    return ollama_generate(prompt).strip()


# ---------------------------------------------------------------------------
# 検索エンジン
# ---------------------------------------------------------------------------

def search_chromadb(
    query: str,
    db_dir: Path,
    top_k: int = TOP_K_VECTOR,
) -> list[tuple[str, float]]:
    """ChromaDB でベクトル検索する。

    Returns:
        [(chunk_id, distance), ...]  distance は cosine distance (小さいほど類似)
    """
    client = chromadb.PersistentClient(path=str(db_dir))
    collection = client.get_collection(COLLECTION_NAME)

    # クエリを embedding に変換
    query_embedding = ollama_embed([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["distances"],
    )

    ids = results["ids"][0]
    distances = results["distances"][0]
    return list(zip(ids, distances))


def search_bm25(
    query: str,
    bm25_dir: Path,
    top_k: int = TOP_K_BM25,
) -> list[tuple[str, float]]:
    """BM25 でキーワード検索する。

    Returns:
        [(chunk_id, score), ...]  score は高いほど関連
    """
    index_path = bm25_dir / "bm25_index.pkl"
    with open(index_path, "rb") as f:
        index_data = pickle.load(f)

    bm25: BM25Okapi = index_data["bm25"]
    chunk_ids: list[str] = index_data["chunk_ids"]
    tokenized: list[list[str]] = index_data["tokenized"]

    # クエリをトークン化（index.py と同じロジック）
    import re
    query_lower = query.lower()
    query_tokens = re.findall(r"[a-z0-9_.]+", query_lower)

    scores = bm25.get_scores(query_tokens)

    # スコア順にソート
    scored = sorted(
        zip(chunk_ids, scores),
        key=lambda x: x[1],
        reverse=True,
    )

    return scored[:top_k]


# ---------------------------------------------------------------------------
# Reciprocal Rank Fusion
# ---------------------------------------------------------------------------

def reciprocal_rank_fusion(
    vector_results: list[tuple[str, float]],
    bm25_results: list[tuple[str, float]],
    k: int = RRF_K,
    top_k: int = TOP_K_FINAL,
) -> list[str]:
    """2 つのランキングを RRF で統合する。

    RRF score = Σ 1 / (k + rank_i)

    Returns:
        統合後の上位 chunk_id リスト
    """
    rrf_scores: dict[str, float] = {}

    for rank, (chunk_id, _) in enumerate(vector_results):
        rrf_scores[chunk_id] = rrf_scores.get(chunk_id, 0) + 1.0 / (k + rank + 1)

    for rank, (chunk_id, _) in enumerate(bm25_results):
        rrf_scores[chunk_id] = rrf_scores.get(chunk_id, 0) + 1.0 / (k + rank + 1)

    sorted_ids = sorted(rrf_scores, key=rrf_scores.get, reverse=True)
    return sorted_ids[:top_k]


# ---------------------------------------------------------------------------
# チャンクの取得
# ---------------------------------------------------------------------------

def load_chunks_by_ids(
    chunk_ids: list[str],
    chunks_dir: Path,
) -> dict[str, dict]:
    """チャンク ID からチャンクデータを取得する。"""
    # 全チャンクをロード（805件なのでメモリに問題なし）
    all_chunks: dict[str, dict] = {}
    for json_path in chunks_dir.glob("Chapter_*.json"):
        data = json.loads(json_path.read_text(encoding="utf-8"))
        for c in data:
            all_chunks[c["chunk_id"]] = c

    return {cid: all_chunks[cid] for cid in chunk_ids if cid in all_chunks}


# ---------------------------------------------------------------------------
# LLM 回答生成
# ---------------------------------------------------------------------------

def generate_answer(query: str, chunks: list[dict]) -> str:
    """検索結果のチャンクを使って LLM で回答を生成する。"""
    # コンテキストの構築
    context_parts = []
    for i, c in enumerate(chunks, 1):
        header = f"[{i}] Chapter {c['chapter']}"
        if c["section"]:
            header += f", Section {c['section']}"
        if c["section_title"]:
            header += f": {c['section_title']}"

        eq_info = ""
        eq_nums = [n for n in c.get("equation_numbers", []) if n]
        if eq_nums:
            eq_info = f"\nEquations: {', '.join(eq_nums)}"

        context_parts.append(f"{header}{eq_info}\n{c['text']}")

    context = "\n\n---\n\n".join(context_parts)

    system_prompt = (
        "You are a helpful assistant specialized in Hapke's "
        "Theory of Reflectance and Emittance Spectroscopy. "
        "Answer the user's question based on the provided context. "
        "Always cite the source using [N] notation. "
        "If the question is in Japanese, answer in Japanese. "
        "If the question is in English, answer in English. "
        "Include relevant equations in LaTeX format when applicable."
    )

    prompt = (
        f"Context:\n{context}\n\n"
        f"Question: {query}\n\n"
        "Answer:"
    )

    return ollama_generate(prompt, system=system_prompt)


# ---------------------------------------------------------------------------
# CLI 表示
# ---------------------------------------------------------------------------

def print_results(
    query: str,
    query_en: str | None,
    final_ids: list[str],
    chunks: dict[str, dict],
    vector_results: list[tuple[str, float]],
    bm25_results: list[tuple[str, float]],
) -> None:
    """検索結果を整形して表示する。"""
    print(f"\n{'='*60}")
    print(f"クエリ: {query}")
    if query_en and query_en != query:
        print(f"英訳:   {query_en}")
    print(f"{'='*60}\n")

    # ベクトル検索の上位
    print("--- ChromaDB (ベクトル検索) 上位 5 件 ---")
    for rank, (cid, dist) in enumerate(vector_results[:5], 1):
        c = chunks.get(cid, {})
        sec = c.get("section", "?")
        title = c.get("section_title", "?")
        print(f"  {rank}. [{cid}] sec={sec} dist={dist:.4f}  {title}")

    print("\n--- BM25 (キーワード検索) 上位 5 件 ---")
    for rank, (cid, score) in enumerate(bm25_results[:5], 1):
        c = chunks.get(cid, {})
        sec = c.get("section", "?")
        title = c.get("section_title", "?")
        print(f"  {rank}. [{cid}] sec={sec} score={score:.4f}  {title}")

    print(f"\n--- RRF 統合結果 (上位 {len(final_ids)} 件) ---")
    for rank, cid in enumerate(final_ids, 1):
        c = chunks.get(cid, {})
        sec = c.get("section", "?")
        title = c.get("section_title", "?")
        tokens = c.get("token_count", 0)
        eq_nums = [n for n in c.get("equation_numbers", []) if n]
        eq_str = f"  eqs={','.join(eq_nums)}" if eq_nums else ""
        print(f"  {rank}. [{cid}] Ch.{c.get('chapter','?')} "
              f"sec={sec} ({tokens} tok){eq_str}")
        # テキストの先頭を表示
        text_preview = c.get("text", "")[:120].replace("\n", " ")
        print(f"     {text_preview}...")

    print()


# ---------------------------------------------------------------------------
# メイン
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Hapke RAG 検索")
    parser.add_argument("--query", "-q", required=True, help="検索クエリ")
    parser.add_argument("--no-llm", action="store_true",
                        help="LLM 回答生成をスキップ（検索結果のみ表示）")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent.parent
    db_dir = base / "db"
    bm25_dir = base / "bm25"
    chunks_dir = base / "chunks"

    if not check_ollama():
        print(
            "Error: Ollama が起動していません。\n"
            "  ollama serve &\n"
            "を実行してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    query = args.query

    # 日本語クエリの英訳
    query_en = None
    if _is_japanese(query):
        print("日本語クエリを英訳中...")
        query_en = translate_to_english(query)
        search_query = query_en
    else:
        search_query = query

    # 1. ChromaDB ベクトル検索
    vector_results = search_chromadb(search_query, db_dir)

    # 2. BM25 キーワード検索
    bm25_results = search_bm25(search_query, bm25_dir)

    # 3. RRF 統合
    final_ids = reciprocal_rank_fusion(vector_results, bm25_results)

    # チャンクデータの取得
    all_needed_ids = set(final_ids)
    all_needed_ids.update(cid for cid, _ in vector_results[:5])
    all_needed_ids.update(cid for cid, _ in bm25_results[:5])
    chunks = load_chunks_by_ids(list(all_needed_ids), chunks_dir)

    # 結果表示
    print_results(query, query_en, final_ids, chunks,
                  vector_results, bm25_results)

    # 4. LLM 回答生成
    if not args.no_llm:
        print("--- Qwen2.5 で回答生成中... ---\n")
        answer_chunks = [chunks[cid] for cid in final_ids if cid in chunks]
        answer = generate_answer(query, answer_chunks)
        print(answer)
        print()


if __name__ == "__main__":
    main()
