#!/usr/bin/env python3
"""clean.py — Marker 出力 Markdown の品質正規化

Marker 1.10.2 (surya) が生成した Markdown ファイルに含まれる
OCR 起因の品質問題を正規化し、chunk.py の入力として適切な
Markdown を生成する。

入力: extracted/marker/Chapter_*/Chapter_*.md (17 ファイル)
出力: extracted/cleaned/Chapter_*.md (17 ファイル)
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# 統計カウンタ
# ---------------------------------------------------------------------------

@dataclass
class RuleStats:
    """章ごとのルール適用件数を記録する。"""
    rule1_html_tags: int = 0
    rule2_sup_sub: int = 0
    rule3_excl_degree: int = 0
    rule3_excl_exponent: int = 0
    rule4_heading: int = 0
    rule5_links: int = 0
    rule6_images: int = 0
    rule7_warnings: list[str] = field(default_factory=list)

    def total(self) -> int:
        return (
            self.rule1_html_tags
            + self.rule2_sup_sub
            + self.rule3_excl_degree
            + self.rule3_excl_exponent
            + self.rule4_heading
            + self.rule5_links
            + self.rule6_images
        )


# ---------------------------------------------------------------------------
# LaTeX 領域の保護
# ---------------------------------------------------------------------------

_LATEX_PLACEHOLDER = "\x00LATEX{}\x00"

def _protect_latex(text: str) -> tuple[str, list[str]]:
    """$...$ および $$...$$ を一時的にプレースホルダに置換する。

    ルール 1–3 が LaTeX 内部を破壊しないようにするため。
    """
    store: list[str] = []

    def _replace(m: re.Match) -> str:
        idx = len(store)
        store.append(m.group(0))
        return _LATEX_PLACEHOLDER.format(idx)

    # $$...$$ を先に処理（$...$ より貪欲にマッチさせないため）
    text = re.sub(r"\$\$.*?\$\$", _replace, text, flags=re.DOTALL)
    # $...$（改行を含まない）
    text = re.sub(r"\$(?!\$)(?:[^$\n]|\\\$)+?\$", _replace, text)
    return text, store


def _restore_latex(text: str, store: list[str]) -> str:
    """プレースホルダを元の LaTeX に復元する。"""
    for i, original in enumerate(store):
        placeholder = _LATEX_PLACEHOLDER.format(i)
        text = text.replace(placeholder, original)
    return text


# ---------------------------------------------------------------------------
# ルール 2: <sup> / <sub> の処理
# ---------------------------------------------------------------------------

def _apply_rule2(text: str, stats: RuleStats) -> str:
    """<sup>/<sub> タグを処理する。

    パターン A: <sup>数値</sup>!<sup>数値</sup> → $数値^{-数値}$
    パターン B: 残りの <sup>X</sup> → X, <sub>X</sub> → X
    """
    # パターン A: <sup>10</sup>!<sup>3</sup> のような指数表記
    # 前に数値がある場合も考慮: 10<sup>!</sup><sup>3</sup> 等の変種にも対応
    def _fix_sup_exponent(m: re.Match) -> str:
        stats.rule2_sup_sub += 1
        base = m.group(1)
        exp = m.group(2)
        return f"$10^{{-{exp}}}$" if base == "10" else f"${base}^{{-{exp}}}$"

    # <sup>BASE</sup>!<sup>EXP</sup>
    text = re.sub(
        r"<sup>(\d+)</sup>\s*!\s*<sup>(\d+)</sup>",
        _fix_sup_exponent,
        text,
    )

    # パターン B: 残りの <sup>X</sup> → X
    def _strip_sup(m: re.Match) -> str:
        stats.rule2_sup_sub += 1
        return m.group(1)

    text = re.sub(r"<sup>(.*?)</sup>", _strip_sup, text)

    # <sub>X</sub> → X
    def _strip_sub(m: re.Match) -> str:
        stats.rule2_sup_sub += 1
        return m.group(1)

    text = re.sub(r"<sub>(.*?)</sub>", _strip_sub, text)

    return text


# ---------------------------------------------------------------------------
# ルール 3: ! の文字化け修正
# ---------------------------------------------------------------------------

def _apply_rule3(text: str, stats: RuleStats) -> str:
    """! が度記号 ° やマイナス記号に化けている箇所を修正する。

    パターン A: 数値! → 数値°（数値直後の ! で後ろがスペース・句読点・行末・*）
    パターン B: 10!N → $10^{-N}$（ルール 2 で未処理の残存パターン）
    """
    # パターン B: 10!N (数字!数字) → $10^{-N}$
    def _fix_exponent(m: re.Match) -> str:
        stats.rule3_excl_exponent += 1
        base = m.group(1)
        exp = m.group(2)
        return f"${base}^{{-{exp}}}$"

    text = re.sub(r"\b(\d+)!(\d+)\b", _fix_exponent, text)

    # パターン A: 数値! → 数値°
    def _fix_degree(m: re.Match) -> str:
        stats.rule3_excl_degree += 1
        return m.group(1) + "°" + m.group(2)

    # 数値の直後に ! が来て、その後にスペース・句読点・行末・* が続く場合
    text = re.sub(
        r"(\d(?:\.\d+)?)!([\s,.*);:\"]|$)",
        _fix_degree,
        text,
        flags=re.MULTILINE,
    )

    return text


# ---------------------------------------------------------------------------
# ルール 1: HTML タグの除去
# ---------------------------------------------------------------------------

def _apply_rule1(text: str, stats: RuleStats) -> str:
    """<span id="...">, </span>, <br>, <br/> を除去する。"""
    count = 0

    def _count_and_remove(m: re.Match) -> str:
        nonlocal count
        count += 1
        return ""

    text = re.sub(r"<span\s+id=\"[^\"]*\">\s*</span>", _count_and_remove, text)
    text = re.sub(r"<span\s+id=\"[^\"]*\">", _count_and_remove, text)
    text = re.sub(r"</span>", _count_and_remove, text)
    text = re.sub(r"<br\s*/?>", _count_and_remove, text)

    stats.rule1_html_tags += count
    return text


# ---------------------------------------------------------------------------
# ルール 4: 見出しレベルの正規化
# ---------------------------------------------------------------------------

# 章番号: "Chapter N", "**N**", 単独の数字
_RE_CHAPTER = re.compile(
    r"^(?:Chapter\s+)?(\d+)$"
    r"|^(\d+)$",
    re.IGNORECASE,
)

# 節番号: N.M（2 レベル）
_RE_SECTION = re.compile(r"(\d+)\.(\d+)\b")

# 小節番号: N.M.K（3 レベル）
_RE_SUBSECTION = re.compile(r"(\d+)\.(\d+)\.(\d+)\b")


def _clean_heading_text(text: str) -> str:
    """見出しテキストから **太字** と *斜体* の装飾を除去する。"""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    return text.strip()


def _apply_rule4(lines: list[str], stats: RuleStats) -> list[str]:
    """見出しレベルを正規化する。

    - 章番号のみ → # (H1)
    - N.M → ## (H2)
    - N.M.K → ### (H3)
    - 上記に該当しない見出し → 現在のレベルを維持
    """
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        heading_match = re.match(r"^(#{1,6})\s+(.*)", line)

        if not heading_match:
            result.append(line)
            i += 1
            continue

        hashes = heading_match.group(1)
        raw_text = heading_match.group(2)
        cleaned = _clean_heading_text(raw_text)

        # 章番号のみの見出しか判定
        is_chapter_number_only = bool(
            re.match(r"^(?:Chapter\s+)?\d+\s*$", cleaned, re.IGNORECASE)
        )

        # 章番号のみの見出しの場合、後続の番号なし見出しをマージする
        # パターン: "## **14**" → (空行) → "### Reflectance spectroscopy"
        if is_chapter_number_only:
            # 空行をスキップして次の見出しを探す
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines):
                next_heading = re.match(r"^(#{1,6})\s+(.*)", lines[j])
                if next_heading:
                    next_text = _clean_heading_text(next_heading.group(2))
                    # 次の見出しに節番号がなければ章タイトルの続きとみなす
                    if (
                        not _RE_SECTION.search(next_text)
                        and not _RE_SUBSECTION.search(next_text)
                        and not re.match(
                            r"^(?:Chapter\s+)?\d+\s*$",
                            next_text,
                            re.IGNORECASE,
                        )
                    ):
                        cleaned = f"{cleaned} {next_text}"
                        stats.rule4_heading += 1
                        # i+1 から j までの行（空行 + マージされた見出し）をスキップ
                        i = j + 1
                        result.append(f"# {cleaned}")
                        continue

        # 見出しテキストの先頭にある番号パターンでレベルを判定する。
        # 先頭を基準にすることで、「14.3 ... 14.3.1 ...」のような
        # 節タイトルと小節タイトルが同一行にある場合に、先頭の 14.3 で
        # ## と判定できる。
        leading_subsection = re.match(r"^\s*(\d+\.\d+\.\d+)\b", cleaned)
        leading_section = re.match(r"^\s*(\d+\.\d+)\b", cleaned)

        if leading_subsection:
            new_level = "###"
        elif leading_section:
            new_level = "##"
        elif is_chapter_number_only:
            new_level = "#"
        else:
            # 番号が検出できない見出し → 現在のレベルを維持
            new_level = hashes

        if new_level != hashes or cleaned != raw_text:
            stats.rule4_heading += 1

        result.append(f"{new_level} {cleaned}")
        i += 1

    return result


# ---------------------------------------------------------------------------
# ルール 5: Markdown リンクの簡素化
# ---------------------------------------------------------------------------

def _apply_rule5(text: str, stats: RuleStats) -> str:
    """[テキスト](#page-...) → テキスト（画像リンクは保持）。

    エスケープされた括弧 \\( \\) も除去する。
    """
    def _simplify_link(m: re.Match) -> str:
        stats.rule5_links += 1
        link_text = m.group(1)
        # \\( と \\) を除去（Marker が式番号参照に付加する）
        link_text = link_text.replace("\\(", "(").replace("\\)", ")")
        return link_text

    # 画像リンク ![...](...) を先に保護
    # 否定先読みで ! の直後でないことを確認
    text = re.sub(
        r"(?<!!)\[([^\]]*)\]\(#page-[^)]*\)",
        _simplify_link,
        text,
    )
    return text


# ---------------------------------------------------------------------------
# ルール 6: 画像参照行の正規化
# ---------------------------------------------------------------------------

def _apply_rule6(text: str, stats: RuleStats) -> str:
    """![alt](_page_N_...) → <!-- IMAGE: filename -->"""

    def _normalize_image(m: re.Match) -> str:
        stats.rule6_images += 1
        filename = m.group(2)
        return f"<!-- IMAGE: {filename} -->"

    text = re.sub(
        r"!\[([^\]]*)\]\(([^)]+\.(?:jpeg|jpg|png|gif|svg|webp))\)",
        _normalize_image,
        text,
        flags=re.IGNORECASE,
    )
    return text


# ---------------------------------------------------------------------------
# ルール 7: スペース欠落の検出（フラグ付けのみ）
# ---------------------------------------------------------------------------

# camelCase の一般的なパターンを除外するための既知語
_CAMELCASE_KNOWN = {
    "JavaScript", "TypeScript", "GitHub", "LaTeX", "BaSO",
    "MgO", "KBr", "McDonald", "McCord", "MacBook",
    "PyTorch", "DataFrame", "NumPy",
}


def _apply_rule7(
    text: str, chapter_name: str, stats: RuleStats
) -> None:
    """小文字→大文字の連続でスペース欠落を検出し警告する。"""
    for line_num, line in enumerate(text.splitlines(), start=1):
        # LaTeX 行・見出し行・画像行・コメント行はスキップ
        if line.strip().startswith(("$", "#", "!", "<!--")):
            continue

        # 小文字の直後に大文字が来る箇所を検出（3文字以上の連続）
        for m in re.finditer(r"[a-z]{2,}[A-Z][a-z]{2,}", line):
            word = m.group(0)
            # 既知の camelCase は除外
            if any(known in word for known in _CAMELCASE_KNOWN):
                continue
            # ハイフン後の大文字は正常（例: near-IR）
            # → この正規表現ではハイフン後はマッチしないので問題ない

            stats.rule7_warnings.append(
                f"  {chapter_name}:{line_num}: ...{word}..."
            )


# ---------------------------------------------------------------------------
# メインパイプライン
# ---------------------------------------------------------------------------

def clean_chapter(text: str, chapter_name: str) -> tuple[str, RuleStats]:
    """1 章分の Markdown を正規化する。"""
    stats = RuleStats()

    # LaTeX 領域を保護
    text, latex_store = _protect_latex(text)

    # ルール 2: <sup>/<sub> 処理（ルール 1 より先）
    text = _apply_rule2(text, stats)

    # ルール 3: ! 文字化け修正（ルール 2 の後）
    text = _apply_rule3(text, stats)

    # ルール 1: HTML タグ除去（ルール 2 の後）
    text = _apply_rule1(text, stats)

    # LaTeX 領域を復元
    text = _restore_latex(text, latex_store)

    # ルール 5: Markdown リンク簡素化
    text = _apply_rule5(text, stats)

    # ルール 6: 画像参照正規化
    text = _apply_rule6(text, stats)

    # ルール 4: 見出しレベル正規化（行単位処理）
    lines = text.splitlines()
    lines = _apply_rule4(lines, stats)
    text = "\n".join(lines)

    # ルール 7: スペース欠落検出（最後に適用）
    _apply_rule7(text, chapter_name, stats)

    return text, stats


def main() -> None:
    base = Path(__file__).resolve().parent.parent
    marker_dir = base / "extracted" / "marker"
    cleaned_dir = base / "extracted" / "cleaned"
    cleaned_dir.mkdir(parents=True, exist_ok=True)

    # 入力ファイルを収集
    md_files = sorted(marker_dir.glob("Chapter_*/Chapter_*.md"))
    if not md_files:
        print(f"Error: {marker_dir} に Chapter_*.md が見つかりません",
              file=sys.stderr)
        sys.exit(1)

    print(f"=== clean.py: {len(md_files)} 章を処理 ===\n")

    all_warnings: list[str] = []
    total_changes = 0

    for md_path in md_files:
        chapter_name = md_path.stem  # e.g. "Chapter_5"
        text = md_path.read_text(encoding="utf-8")

        cleaned, stats = clean_chapter(text, chapter_name)

        # 出力
        out_path = cleaned_dir / f"{chapter_name}.md"
        out_path.write_text(cleaned, encoding="utf-8")

        # レポート
        changes = stats.total()
        total_changes += changes
        print(f"{chapter_name}: {changes} 件の変更")
        if stats.rule1_html_tags:
            print(f"  ルール 1 (HTML タグ除去):    {stats.rule1_html_tags}")
        if stats.rule2_sup_sub:
            print(f"  ルール 2 (<sup>/<sub> 処理): {stats.rule2_sup_sub}")
        if stats.rule3_excl_degree:
            print(f"  ルール 3a (! → °):           {stats.rule3_excl_degree}")
        if stats.rule3_excl_exponent:
            print(f"  ルール 3b (N!M → 指数):      {stats.rule3_excl_exponent}")
        if stats.rule4_heading:
            print(f"  ルール 4 (見出し正規化):     {stats.rule4_heading}")
        if stats.rule5_links:
            print(f"  ルール 5 (リンク簡素化):     {stats.rule5_links}")
        if stats.rule6_images:
            print(f"  ルール 6 (画像参照正規化):   {stats.rule6_images}")

        if stats.rule7_warnings:
            all_warnings.extend(stats.rule7_warnings)

    print(f"\n合計: {total_changes} 件の変更, {len(md_files)} 章を出力")
    print(f"出力先: {cleaned_dir}/")

    if all_warnings:
        print(f"\n=== ルール 7: スペース欠落の疑い ({len(all_warnings)} 件) ===")
        for w in all_warnings:
            print(w)


if __name__ == "__main__":
    main()
