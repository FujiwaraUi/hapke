# Hapke RAG: 抽出完了後の次ステップ

## 0. 変換結果の確認

```bash
# 全章の OK/FAIL/SKIP を確認
cat shell/result.txt | grep -E "OK|FAIL|SKIP"

# .md ファイルの一覧
ls extracted/marker/*/Chapter_*.md

# FAIL があった場合: 該当ディレクトリを削除して shell.sh を再実行
# rm -rf extracted/marker/Chapter_X
# nohup bash ./shell/shell.sh > shell/nohup.out 2>&1 &
```

## 1. 数式品質のスポットチェック

Chapter 2 は確認済み。数式が多い章を 2〜3 章選んで目視確認する。

候補: Chapter 5（散乱）、Chapter 8（双方向反射率）、Chapter 10（反射率モデル）

```bash
head -100 extracted/marker/Chapter_5/Chapter_5.md
head -100 extracted/marker/Chapter_8/Chapter_8.md
head -100 extracted/marker/Chapter_10/Chapter_10.md
```

確認観点:

- LaTeX 数式（`$...$`, `$$...$$`）が保持されているか
- 節見出し（`#`, `##`）の階層が原書と一致しているか
- 図表キャプションが本文と分離されているか
- 式番号（例: `(2.34)`）が残っているか

## 2. チャンク分割（chunk.py）

### 設計方針（実装前に決定する）

| 項目 | 選択肢 | 推奨 |
|------|--------|------|
| 分割境界 | 固定トークン数 / 見出し単位 / 段落単位 | 見出し（`##`, `###`）を一次境界、段落を二次境界 |
| チャンクサイズ | 300〜500 トークン | 400 トークン目安、数式ブロックは途中で切断しない |
| オーバーラップ | 0 / 50〜100 トークン | 50 トークン（文脈維持のため） |
| メタデータ | 章番号, 節番号, 節タイトル, 式番号 | 全て付与 |
| 数式の自然言語記述 | 手動 / LLM 自動生成 / なし | LLM 自動生成（Qwen2.5 で後処理） |

### 出力形式（案）

```json
{
  "chunk_id": "ch08_sec03_p02",
  "chapter": 8,
  "section": "8.3",
  "section_title": "The Bidirectional Reflectance",
  "text": "The bidirectional reflectance r is defined as ...",
  "equations": ["r = \\frac{w}{4\\pi} \\frac{1}{\\mu_0 + \\mu} ..."],
  "equation_numbers": ["(8.12)"],
  "equation_descriptions": ["双方向反射率 r の定義式。..."],
  "token_count": 387
}
```

### 実装

```bash
# Ollama を起動（数式の自然言語記述に使用）
ollama serve &
# → 数式記述の自動生成を行わない場合は不要

# chunk.py を実装後に実行
.venv/bin/python3 hapke_rag/chunk.py
# 入力: extracted/marker/Chapter_*/Chapter_*.md
# 出力: chunks/*.json
```

## 3. Embedding + ChromaDB 格納（index.py）

```bash
# Ollama で nomic-embed-text を準備
ollama pull nomic-embed-text

# index.py を実装後に実行
.venv/bin/python3 hapke_rag/index.py
# 入力: chunks/*.json
# 出力: db/（ChromaDB 永続データ）+ bm25/（BM25 インデックス）
```

ChromaDB と BM25 の構築は同一スクリプトで行う（チャンクの読み込みが共通のため）。

## 4. Hybrid 検索 + LLM 回答（search.py）

```bash
# Ollama で qwen2.5:7b を起動
ollama run qwen2.5:7b

# CLI で動作確認
.venv/bin/python3 hapke_rag/search.py --query "双方向反射率の定義"
```

検索パイプライン:

1. クエリが日本語なら Qwen2.5 で英訳
2. ChromaDB ベクトル検索（上位 10 件）
3. BM25 キーワード検索（上位 10 件）
4. Reciprocal Rank Fusion で上位 5 件に絞込
5. Qwen2.5 で回答生成 + 出典明示

## 5. Gradio UI（app.py）

```bash
.venv/bin/python3 hapke_rag/app.py
# → http://localhost:7860 でアクセス
# MacBook からは http://192.168.0.200:7860
```

数式レンダリングは Gradio の Markdown コンポーネント（KaTeX 対応）を使用。

## 作業順序まとめ

```
[現在] Marker 全章変換（実行中）
  │
  ▼
[次] 変換結果の確認（品質スポットチェック）
  │
  ▼
chunk.py 実装 → chunks/*.json 生成
  │
  ▼
index.py 実装 → db/ + bm25/ 構築
  │
  ▼
search.py 実装 → CLI で検索動作確認
  │
  ▼
app.py 実装 → Gradio UI で利用開始
```
