#!/usr/bin/env bash
set -uo pipefail

# ---- 設定 ----
PROJECT_DIR="/home/fy/user/knowledge/hapke"
VENV_BIN="$PROJECT_DIR/.venv/bin"
PDF_DIR="$PROJECT_DIR/pdf"
OUT_DIR="$PROJECT_DIR/extracted/marker"
LOG_FILE="$PROJECT_DIR/shell/result.txt"

export PATH="$VENV_BIN:$PATH"

mkdir -p "$OUT_DIR"
mkdir -p "$(dirname "$LOG_FILE")"

echo "=== Marker batch conversion started: $(date) ===" | tee "$LOG_FILE"

# ---- 変換ループ ----
for pdf in "$PDF_DIR"/Chapter_*.pdf; do
    basename_noext=$(basename "$pdf" .pdf)
    echo "--- Processing: $basename_noext ---" | tee -a "$LOG_FILE"

    # 変換済みディレクトリが存在し .md ファイルがあればスキップ
    if [ -d "$OUT_DIR/$basename_noext" ] && [ -f "$OUT_DIR/$basename_noext/${basename_noext}.md" ]; then
	echo "  SKIP: $basename_noext (already exists)" | tee -a "$LOG_FILE"
	continue
    fi

    # marker_single で変換
    # --layout_batch_size, --recognition_batch_size: VRAM 8GB での OOM 対策
    # --disable_multiprocessing: メモリ使用量を抑制
    if marker_single "$pdf" \
		     --output_dir "$OUT_DIR" \
		     --layout_batch_size 2 \
		     --recognition_batch_size 2 \
		     --equation_batch_size 2 \
		     --disable_multiprocessing \
		     2>&1 | tee -a "$LOG_FILE"; then
	echo "  OK: $basename_noext" | tee -a "$LOG_FILE"
    else
	echo "  FAIL: $basename_noext (exit code: $?)" | tee -a "$LOG_FILE"
    fi
done

# ---- ディレクトリ名・ファイル名の空白をアンダースコアに置換 ----
echo "--- Renaming spaces to underscores ---" | tee -a "$LOG_FILE"

# ディレクトリ名を先に処理（深い階層から）
find "$OUT_DIR" -depth -name "* *" -type d | while IFS= read -r dir; do
    parent=$(dirname "$dir")
    oldname=$(basename "$dir")
    newname="${oldname// /_}"
    mv -v "$dir" "$parent/$newname" 2>&1 | tee -a "$LOG_FILE"
done

# ファイル名を処理
find "$OUT_DIR" -name "* *" -type f | while IFS= read -r file; do
    parent=$(dirname "$file")
    oldname=$(basename "$file")
    newname="${oldname// /_}"
    mv -v "$file" "$parent/$newname" 2>&1 | tee -a "$LOG_FILE"
done

echo "=== Marker batch conversion finished: $(date) ===" | tee -a "$LOG_FILE"
