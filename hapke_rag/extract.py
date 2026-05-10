#!/usr/bin/env python3
"""PDF → テキスト抽出（pymupdf）

各章PDFからテキストを抽出し、ページ番号付きのJSONとして保存する。
"""

import json
import re
import sys
from pathlib import Path

import fitz  # pymupdf


def extract_chapter_number(filename: str) -> int | None:
    """ファイル名から章番号を抽出する。"""
    m = re.match(r"Chapter\s+(\d+)", filename)
    return int(m.group(1)) if m else None


def extract_pdf(pdf_path: Path) -> list[dict]:
    """1つのPDFからページごとのテキストを抽出する。"""
    doc = fitz.open(pdf_path)
    pages = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")
        if text.strip():
            pages.append({
                "page": page_num,
                "text": text.strip(),
            })
    doc.close()
    return pages


def process_all(pdf_dir: Path, output_dir: Path) -> None:
    """pdf/ 以下の全Chapter PDFを処理し、extracted/ にJSONを出力する。"""
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(pdf_dir.glob("Chapter *.pdf"))
    if not pdf_files:
        print(f"Error: {pdf_dir} にChapter PDFが見つかりません", file=sys.stderr)
        sys.exit(1)

    for pdf_path in pdf_files:
        chapter_num = extract_chapter_number(pdf_path.name)
        if chapter_num is None:
            print(f"  スキップ: {pdf_path.name}（章番号を認識できない）")
            continue

        print(f"  処理中: {pdf_path.name} ... ", end="", flush=True)
        pages = extract_pdf(pdf_path)

        output = {
            "source_file": pdf_path.name,
            "chapter": chapter_num,
            "total_pages": len(pages),
            "pages": pages,
        }

        out_path = output_dir / f"chapter_{chapter_num:02d}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

        print(f"{len(pages)} ページ → {out_path.name}")

    print(f"\n完了: {output_dir} に出力しました")


if __name__ == "__main__":
    base = Path(__file__).resolve().parent.parent
    pdf_dir = base / "pdf"
    output_dir = base / "extracted"
    process_all(pdf_dir, output_dir)
