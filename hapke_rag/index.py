#!/usr/bin/env python3
"""index.py — チャンクの Embedding 生成 + ChromaDB / BM25 インデックス構築

chunk.py が生成した chunks/*.json を読み込み、以下を構築する:
  1. ChromaDB コレクション（ベクトル検索用）
  2. BM25 インデックス（キーワード検索用）

Embedding は Ollama の nomic-embed-text をローカルで使用する。

入力: chunks/Chapter_*.json (17 ファイル)
出力: db/    (ChromaDB 永続データ)
      bm25/  (BM25 インデックス, pickle)
"""

from __future__ import annotations

import json
import pickle
import sys
import time
from pathlib import Path

import chromadb
import requests
from rank_bm25 import BM25Okapi


# ---------------------------------------------------------------------------
# 設定
# ---------------------------------------------------------------------------

OLLAMA_BASE_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
COLLECTION_NAME = "hapke_rag"

# Embedding バッチサイズ（Ollama は 1 リクエストに複数テキストを受け付ける）
EMBED_BATCH_SIZE = 32


# ---------------------------------------------------------------------------
# Ollama Embedding API
# ---------------------------------------------------------------------------

def check_ollama() -> bool:
    """Ollama が起動しているか確認する。"""
    try:
        r = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        return r.status_code == 200
    except requests.ConnectionError:
        return False


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Ollama の /api/embed エンドポイントでテキストを embedding に変換する。

    バッチ対応: 複数テキストを一度に送信する。
    """
    resp = requests.post(
        f"{OLLAMA_BASE_URL}/api/embed",
        json={
            "model": EMBED_MODEL,
            "input": texts,
        },
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["embeddings"]


# ---------------------------------------------------------------------------
# チャンク読み込み
# ---------------------------------------------------------------------------

def load_all_chunks(chunks_dir: Path) -> list[dict]:
    """全章の chunks/*.json を読み込んで1つのリストにする。"""
    all_chunks: list[dict] = []
    for json_path in sorted(chunks_dir.glob("Chapter_*.json")):
        data = json.loads(json_path.read_text(encoding="utf-8"))
        all_chunks.extend(data)
    return all_chunks


def build_document_text(chunk: dict) -> str:
    """検索用のドキュメントテキストを構築する。

    本文に加え、式番号をテキストとして含めることで
    BM25 でも式番号による完全一致検索が可能になる。
    """
    parts = [chunk["text"]]

    # 式番号を追加（BM25 のキーワード検索で式番号を拾えるようにする）
    eq_nums = [n for n in chunk.get("equation_numbers", []) if n]
    if eq_nums:
        parts.append("Equations: " + ", ".join(eq_nums))

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# ChromaDB 構築
# ---------------------------------------------------------------------------

def build_chromadb(
    chunks: list[dict],
    db_dir: Path,
) -> None:
    """ChromaDB コレクションを構築する。"""
    db_dir.mkdir(parents=True, exist_ok=True)

    client = chromadb.PersistentClient(path=str(db_dir))

    # 既存コレクションがあれば削除して再構築
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    # バッチ処理
    total = len(chunks)
    print(f"\nChromaDB: {total} チャンクの embedding を生成中...")

    for batch_start in range(0, total, EMBED_BATCH_SIZE):
        batch_end = min(batch_start + EMBED_BATCH_SIZE, total)
        batch = chunks[batch_start:batch_end]

        # ドキュメントテキスト
        documents = [build_document_text(c) for c in batch]

        # Embedding 生成
        embeddings = embed_texts(documents)

        # メタデータ
        metadatas = []
        for c in batch:
            meta = {
                "chapter": c["chapter"],
                "section": c["section"],
                "section_title": c["section_title"],
                "token_count": c["token_count"],
            }
            # 式番号（カンマ区切りの文字列として格納）
            eq_nums = [n for n in c.get("equation_numbers", []) if n]
            if eq_nums:
                meta["equation_numbers"] = ",".join(eq_nums)
            metadatas.append(meta)

        ids = [c["chunk_id"] for c in batch]

        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

        done = batch_end
        elapsed_pct = done / total * 100
        print(f"  {done}/{total} ({elapsed_pct:.0f}%)", end="\r")

    print(f"  {total}/{total} (100%) — 完了")
    print(f"  コレクション '{COLLECTION_NAME}': {collection.count()} 件")


# ---------------------------------------------------------------------------
# BM25 インデックス構築
# ---------------------------------------------------------------------------

def _tokenize_for_bm25(text: str) -> list[str]:
    """BM25 用の簡易トークナイザ。

    英語テキストを小文字化し、空白・句読点で分割する。
    式番号 (8.12) 等も1トークンとして扱えるように括弧を保持する。
    """
    # 小文字化
    text = text.lower()
    # 括弧付き式番号を保護: (8.12) → __eq_8.12__
    import re
    eq_nums = re.findall(r"\(\d+\.\d+[a-z]?\)", text)
    for eq in eq_nums:
        placeholder = eq.replace("(", "__eq_").replace(")", "__")
        text = text.replace(eq, placeholder)

    # 基本的な分割
    tokens = re.findall(r"[a-z0-9_.]+", text)

    # プレースホルダを元に戻す
    restored = []
    for t in tokens:
        if t.startswith("__eq_") and t.endswith("__"):
            restored.append(t.replace("__eq_", "(").replace("__", ")"))
        else:
            restored.append(t)

    return restored


def build_bm25(
    chunks: list[dict],
    bm25_dir: Path,
) -> None:
    """BM25 インデックスを構築して pickle で保存する。"""
    bm25_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nBM25: {len(chunks)} チャンクのインデックスを構築中...")

    # 各チャンクのトークン化
    documents = [build_document_text(c) for c in chunks]
    tokenized = [_tokenize_for_bm25(doc) for doc in documents]

    bm25 = BM25Okapi(tokenized)

    # BM25 オブジェクトとチャンク ID のマッピングを保存
    index_data = {
        "bm25": bm25,
        "chunk_ids": [c["chunk_id"] for c in chunks],
        "documents": documents,
        "tokenized": tokenized,
    }

    out_path = bm25_dir / "bm25_index.pkl"
    with open(out_path, "wb") as f:
        pickle.dump(index_data, f)

    print(f"  保存先: {out_path}")
    print(f"  語彙数: {len(bm25.idf)}")


# ---------------------------------------------------------------------------
# メイン
# ---------------------------------------------------------------------------

def main() -> None:
    base = Path(__file__).resolve().parent.parent
    chunks_dir = base / "chunks"
    db_dir = base / "db"
    bm25_dir = base / "bm25"

    # Ollama 起動確認
    if not check_ollama():
        print(
            "Error: Ollama が起動していません。\n"
            "  ollama serve &\n"
            "を実行してから再度試してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    # チャンク読み込み
    chunks = load_all_chunks(chunks_dir)
    if not chunks:
        print(f"Error: {chunks_dir} にチャンクが見つかりません",
              file=sys.stderr)
        sys.exit(1)

    print(f"=== index.py: {len(chunks)} チャンクを処理 ===")

    # 1. ChromaDB 構築
    t0 = time.time()
    build_chromadb(chunks, db_dir)
    t_chroma = time.time() - t0

    # 2. BM25 構築
    t1 = time.time()
    build_bm25(chunks, bm25_dir)
    t_bm25 = time.time() - t1

    print(f"\n=== 完了 ===")
    print(f"  ChromaDB: {t_chroma:.1f} 秒 → {db_dir}/")
    print(f"  BM25:     {t_bm25:.1f} 秒 → {bm25_dir}/")


if __name__ == "__main__":
    main()
