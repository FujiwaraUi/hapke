#!/usr/bin/env python3
"""chunk.py — 正規化済み Markdown のチャンク分割

clean.py で正規化された Markdown を、RAG 用のチャンク（JSON）に分割する。

分割戦略:
  - 一次境界: 見出し（## 節, ### 小節）
  - 二次境界: 段落（空行区切り）
  - 400 トークン目安、数式ブロックは途中で切断しない
  - 50 トークンのオーバーラップ

入力: extracted/cleaned/Chapter_*.md (17 ファイル)
出力: chunks/Chapter_*.json (17 ファイル)
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# 設定
# ---------------------------------------------------------------------------

TARGET_TOKENS = 400
OVERLAP_TOKENS = 50
# 1 トークン ≈ 4 文字（英語テキストの概算）
CHARS_PER_TOKEN = 4


def estimate_tokens(text: str) -> int:
    """テキストのトークン数を概算する。

    正確なトークナイザを使わず、文字数ベースで概算する。
    nomic-embed-text のトークナイザは概ね 1 token ≈ 4 chars (英語)。
    """
    return max(1, len(text) // CHARS_PER_TOKEN)


# ---------------------------------------------------------------------------
# Markdown パーサ
# ---------------------------------------------------------------------------

@dataclass
class Section:
    """見出しで区切られた1セクション。"""
    level: int            # 1=章, 2=節, 3=小節
    heading: str          # 見出しテキスト（# を除く）
    chapter: int | None = None
    section_num: str = ""       # "8.3" or "8.3.1"
    section_title: str = ""     # "The Bidirectional Reflectance"
    paragraphs: list[str] = field(default_factory=list)


_RE_HEADING = re.compile(r"^(#{1,6})\s+(.*)")
_RE_SECTION_NUM = re.compile(r"^(\d+)\.(\d+)(?:\.(\d+))?\b")
_RE_CHAPTER_NUM = re.compile(r"^(\d+)\b")


def _parse_heading_meta(heading: str) -> tuple[int | None, str, str]:
    """見出しテキストから章番号、節番号、節タイトルを抽出する。

    Returns:
        (chapter_num, section_num, section_title)
    """
    # 小節/節番号: "8.3.1 Title" or "8.3 Title"
    m = _RE_SECTION_NUM.match(heading)
    if m:
        chapter = int(m.group(1))
        if m.group(3):
            sec_num = f"{m.group(1)}.{m.group(2)}.{m.group(3)}"
        else:
            sec_num = f"{m.group(1)}.{m.group(2)}"
        title = heading[m.end():].strip()
        return chapter, sec_num, title

    # 章番号のみ: "14 Reflectance spectroscopy" or "Chapter 14 ..."
    m_chap = re.match(r"^(?:Chapter\s+)?(\d+)\s*(.*)", heading, re.IGNORECASE)
    if m_chap:
        chapter = int(m_chap.group(1))
        title = m_chap.group(2).strip()
        return chapter, "", title

    return None, "", heading


def parse_markdown(text: str) -> list[Section]:
    """Markdown テキストをセクションのリストに分割する。"""
    sections: list[Section] = []
    current: Section | None = None
    current_para_lines: list[str] = []

    def _flush_para() -> None:
        nonlocal current_para_lines
        if current and current_para_lines:
            para = "\n".join(current_para_lines).strip()
            if para:
                current.paragraphs.append(para)
        current_para_lines = []

    for line in text.splitlines():
        hm = _RE_HEADING.match(line)
        if hm:
            # 前のパラグラフを確定
            _flush_para()

            level = len(hm.group(1))
            heading = hm.group(2).strip()
            chapter, sec_num, title = _parse_heading_meta(heading)

            current = Section(
                level=level,
                heading=heading,
                chapter=chapter,
                section_num=sec_num,
                section_title=title,
            )
            sections.append(current)
            continue

        # 空行 → パラグラフ境界
        if line.strip() == "":
            _flush_para()
            continue

        # HTML コメント（画像）はスキップ
        if line.strip().startswith("<!--"):
            continue

        current_para_lines.append(line)

    # 最終パラグラフを確定
    _flush_para()

    return sections


# ---------------------------------------------------------------------------
# 数式の抽出
# ---------------------------------------------------------------------------

_RE_BLOCK_EQ = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
_RE_TAG = re.compile(r"\\tag\{([^}]+)\}")


def extract_equations(text: str) -> tuple[list[str], list[str]]:
    """テキストから $$...$$ のブロック数式と式番号を抽出する。

    Returns:
        (equations, equation_numbers)
    """
    equations: list[str] = []
    equation_numbers: list[str] = []

    for m in _RE_BLOCK_EQ.finditer(text):
        eq_body = m.group(1).strip()
        equations.append(eq_body)

        # \tag{...} 形式を優先
        tag_m = _RE_TAG.search(eq_body)
        if tag_m:
            equation_numbers.append(f"({tag_m.group(1)})")
        else:
            # 末尾に (N.M) や (N.Ma) のような式番号が直接書かれているパターン
            trailing_m = re.search(
                r"\((\d+\.\d+[a-z]?)\)\s*$", eq_body
            )
            if trailing_m:
                equation_numbers.append(f"({trailing_m.group(1)})")
            else:
                equation_numbers.append("")

    return equations, equation_numbers


# ---------------------------------------------------------------------------
# チャンク生成
# ---------------------------------------------------------------------------

@dataclass
class Chunk:
    """1 つのチャンク。"""
    chunk_id: str
    chapter: int
    section: str
    section_title: str
    text: str
    equations: list[str]
    equation_numbers: list[str]
    token_count: int


def _make_chunk_id(chapter: int, section: str, part_idx: int) -> str:
    """チャンク ID を生成する。

    例: ch08_sec03_p02, ch14_sec03_01_p01
    """
    if section:
        parts = section.split(".")
        sec_str = "_".join(f"{int(p):02d}" for p in parts)
        sec_part = f"sec{sec_str}"
    else:
        sec_part = "sec00"
    return f"ch{chapter:02d}_{sec_part}_p{part_idx:02d}"


def _split_paragraphs_into_chunks(
    paragraphs: list[str],
    chapter: int,
    section: str,
    section_title: str,
) -> list[Chunk]:
    """段落リストをトークンサイズに基づいてチャンクに分割する。

    - 数式ブロック ($$...$$) を含む段落は途中で分割しない
    - TARGET_TOKENS を超える場合は段落境界で分割
    - OVERLAP_TOKENS 分の末尾テキストを次のチャンクの先頭に重複させる
    """
    if not paragraphs:
        return []

    chunks: list[Chunk] = []
    current_paras: list[str] = []
    current_tokens = 0
    part_idx = 0

    def _emit_chunk() -> None:
        nonlocal current_paras, current_tokens, part_idx
        if not current_paras:
            return

        text = "\n\n".join(current_paras)
        eqs, eq_nums = extract_equations(text)

        chunks.append(Chunk(
            chunk_id=_make_chunk_id(chapter, section, part_idx),
            chapter=chapter,
            section=section,
            section_title=section_title,
            text=text,
            equations=eqs,
            equation_numbers=eq_nums,
            token_count=estimate_tokens(text),
        ))
        part_idx += 1

        # オーバーラップ: 最後の段落の末尾 OVERLAP_TOKENS 分を次に引き継ぐ
        if current_paras:
            last_para = current_paras[-1]
            overlap_chars = OVERLAP_TOKENS * CHARS_PER_TOKEN
            if len(last_para) > overlap_chars:
                overlap_text = last_para[-overlap_chars:]
                current_paras = [f"...{overlap_text}"]
                current_tokens = estimate_tokens(current_paras[0])
            else:
                current_paras = [last_para]
                current_tokens = estimate_tokens(last_para)
        else:
            current_paras = []
            current_tokens = 0

    for para in paragraphs:
        para_tokens = estimate_tokens(para)

        # 数式を含む段落は分割しない
        has_equation = "$$" in para

        # 現在のチャンクに追加すると TARGET を超える場合
        if current_tokens > 0 and current_tokens + para_tokens > TARGET_TOKENS:
            _emit_chunk()

        # 単一段落が TARGET を大幅に超える場合でも、
        # 数式を含む段落は分割せずそのまま1チャンクにする
        current_paras.append(para)
        current_tokens += para_tokens

    # 残りを最終チャンクとして出力
    if current_paras:
        text = "\n\n".join(current_paras)
        eqs, eq_nums = extract_equations(text)
        chunks.append(Chunk(
            chunk_id=_make_chunk_id(chapter, section, part_idx),
            chapter=chapter,
            section=section,
            section_title=section_title,
            text=text,
            equations=eqs,
            equation_numbers=eq_nums,
            token_count=estimate_tokens(text),
        ))

    return chunks


def chunk_chapter(text: str) -> list[Chunk]:
    """1 章分の Markdown をチャンクに分割する。"""
    sections = parse_markdown(text)
    all_chunks: list[Chunk] = []

    # 章番号を最初のセクションから取得（フォールバック用）
    chapter_num = 0
    for sec in sections:
        if sec.chapter is not None:
            chapter_num = sec.chapter
            break

    # 現在の節情報（小節がない場合の継承用）
    current_section = ""
    current_section_title = ""

    for sec in sections:
        if sec.chapter is not None:
            chapter_num = sec.chapter

        # 節番号の更新
        if sec.section_num:
            # N.M 形式なら現在の節を更新
            parts = sec.section_num.split(".")
            if len(parts) == 2:
                current_section = sec.section_num
                current_section_title = sec.section_title
            # N.M.K はそのまま使う

        sec_num = sec.section_num if sec.section_num else current_section
        sec_title = sec.section_title if sec.section_num else current_section_title

        # 章見出しのみ（段落なし）のセクションはスキップ
        if not sec.paragraphs:
            continue

        chunks = _split_paragraphs_into_chunks(
            paragraphs=sec.paragraphs,
            chapter=chapter_num,
            section=sec_num,
            section_title=sec_title or sec.heading,
        )
        all_chunks.extend(chunks)

    return all_chunks


# ---------------------------------------------------------------------------
# メイン
# ---------------------------------------------------------------------------

def main() -> None:
    base = Path(__file__).resolve().parent.parent
    cleaned_dir = base / "extracted" / "cleaned"
    chunks_dir = base / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(cleaned_dir.glob("Chapter_*.md"))
    if not md_files:
        print(f"Error: {cleaned_dir} に Chapter_*.md が見つかりません",
              file=sys.stderr)
        sys.exit(1)

    print(f"=== chunk.py: {len(md_files)} 章を処理 ===\n")

    total_chunks = 0
    total_equations = 0

    for md_path in md_files:
        chapter_name = md_path.stem
        text = md_path.read_text(encoding="utf-8")

        chunks = chunk_chapter(text)

        # JSON 出力
        out_data = []
        ch_equations = 0
        for c in chunks:
            ch_equations += len(c.equations)
            out_data.append({
                "chunk_id": c.chunk_id,
                "chapter": c.chapter,
                "section": c.section,
                "section_title": c.section_title,
                "text": c.text,
                "equations": c.equations,
                "equation_numbers": c.equation_numbers,
                "token_count": c.token_count,
            })

        out_path = chunks_dir / f"{chapter_name}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(out_data, f, ensure_ascii=False, indent=2)

        total_chunks += len(chunks)
        total_equations += ch_equations
        print(
            f"{chapter_name}: {len(chunks)} チャンク, "
            f"{ch_equations} 数式"
        )

    print(f"\n合計: {total_chunks} チャンク, {total_equations} 数式")
    print(f"出力先: {chunks_dir}/")

    # トークン分布の概要
    all_tokens: list[int] = []
    for json_path in sorted(chunks_dir.glob("Chapter_*.json")):
        data = json.loads(json_path.read_text(encoding="utf-8"))
        all_tokens.extend(c["token_count"] for c in data)

    if all_tokens:
        avg = sum(all_tokens) / len(all_tokens)
        mn, mx = min(all_tokens), max(all_tokens)
        print(f"\nトークン数: 平均 {avg:.0f}, 最小 {mn}, 最大 {mx}")
        # 分布のバケット
        buckets = {"0-200": 0, "200-400": 0, "400-600": 0, "600+": 0}
        for t in all_tokens:
            if t < 200:
                buckets["0-200"] += 1
            elif t < 400:
                buckets["200-400"] += 1
            elif t < 600:
                buckets["400-600"] += 1
            else:
                buckets["600+"] += 1
        print("分布:")
        for k, v in buckets.items():
            pct = v / len(all_tokens) * 100
            print(f"  {k:>8s}: {v:4d} ({pct:5.1f}%)")


if __name__ == "__main__":
    main()
