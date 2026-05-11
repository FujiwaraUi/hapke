# Hapke RAG

Hapke *Theory of Reflectance and Emittance Spectroscopy*（2nd ed., Cambridge, 2012）を知識ベースとする Hybrid RAG システム。

## 目的

- Hapke 理論の特定の式・定義をクエリで検索する
- 論文執筆時に関連する節・数式を引用可能な形で参照する
- 日本語クエリで英語テキストを検索する（クロスリンガル検索）
- 将来的に Web 検索と統合し、ローカル知識 + 外部情報を重ね合わせて回答する

## 実行環境

| 項目 | 内容 |
|------|------|
| マシン | 自作 PC（Intel i7-6700K, GTX 1080 8GB VRAM, RAM 48GB DDR4） |
| OS | Ubuntu 22.04.5 LTS |
| GPU ドライバ | NVIDIA 535.288.01, CUDA 12.2 |
| Python | 3.12.13（uv で管理） |
| PyTorch | 2.7.1+cu118 |
| PDF 抽出 | Marker 1.10.2（surya ベース、数式を LaTeX 形式で保持） |
| LLM | Ollama + Qwen2.5:7b（ローカル推論） |
| Embedding | Ollama + nomic-embed-text（ローカル推論） |
| 接続 | MacBook Air M3 から SSH + VSCode Remote |

### VRAM 制約

GTX 1080 の実効 VRAM は約 7.7GB（デスクトップ環境が約 415MB 使用）。
Marker と LLM の同時実行は不可。以下の順序で処理する。

1. Marker で全章 PDF を変換（`ollama stop qwen2.5:7b` で VRAM 解放）
2. 変換完了後、RAG パイプライン（Embedding + LLM 推論）を実行

## アーキテクチャ

```
PDF（章ごと, Chapter_0.pdf 〜 Chapter_16.pdf）
  │
  ├─→ Marker（テキスト + 数式を Markdown + LaTeX 形式で抽出）
  │
  ▼
チャンク分割（章 > 節 > 段落, 300–500 トークン）
  + メタデータ（章番号, 節番号, 節タイトル, ページ番号）
  + 数式の自然言語記述（embedding 精度向上のため）
  │
  ├─→ nomic-embed-text → ChromaDB（ベクトル検索）
  ├─→ BM25 インデックス（キーワード完全一致: 式番号, 略語, 固有名詞）
  │
  ▼
クエリ → 日英翻訳（日本語クエリの場合）
  ├─→ ChromaDB 検索（上位 10 件）
  ├─→ BM25 検索（上位 10 件）
  ▼
Reciprocal Rank Fusion（上位 5 件に絞込）
  │
  ▼
Qwen2.5-7B（Ollama 経由, 回答生成 + 出典明示）
  │
  ▼
Gradio UI（検索ボックス + 回答表示 + 出典チャンク + 数式レンダリング）
```

## ディレクトリ構成

```
~/user/knowledge/hapke/
├── .venv/                 # Python 3.12, marker-pdf 1.10.2, torch 2.7.1+cu118
├── pdf/                   # Chapter_0.pdf 〜 Chapter_16.pdf + 全体版 PDF
├── extracted/
│   └── marker/            # Marker 出力（章ごとのサブディレクトリ）
│       ├── Chapter_0/
│       ├── Chapter_1/
│       │   ...
│       └── Chapter_16/
├── chunks/                # チャンク分割後の JSON（未作成）
├── db/                    # ChromaDB 永続データ（未作成）
├── bm25/                  # BM25 インデックス（未作成）
├── hapke_rag/             # Python スクリプト群
│   ├── extract.py         # pymupdf 版（Marker に移行済み）
│   ├── chunk.py           # 未実装
│   ├── index.py           # 未実装
│   ├── search.py          # 未実装
│   └── app.py             # Gradio UI（未実装）
├── shell/
│   ├── shell.sh           # 全章一括変換スクリプト
│   └── result.txt         # 変換ログ
├── pyproject.toml
├── uv.lock
└── README.md
```

## 実装状況

| ステップ | 状態 | 備考 |
|----------|------|------|
| PDF 抽出（Marker） | 実行中 | Chapter_2 で品質確認済み、全章一括変換を `nohup` で実行中 |
| チャンク分割 | 未着手 | Marker の .md 出力に対応する `chunk.py` を作成予定 |
| Embedding + ChromaDB | 未着手 | nomic-embed-text（Ollama）を使用予定 |
| BM25 インデックス | 未着手 | rank-bm25 を使用予定 |
| Hybrid 検索 + LLM 回答 | 未着手 | Reciprocal Rank Fusion + Qwen2.5-7B |
| Gradio UI | 未着手 | KaTeX/MathJax で数式レンダリング |
| Web 検索統合 | 未着手 | 将来対応 |

## PDF 抽出ツールの選定経緯

| ツール | 結果 |
|--------|------|
| pymupdf | 数式が平坦化される（∂ → ζ の文字化け、LaTeX 形式で出力されない）。不採用 |
| Nougat | 数式品質は高いが、モデル重み約 6GB で 8GB VRAM では OOM リスクが高い。不採用 |
| Marker 1.10.2 | surya ベースの軽量モデル群で VRAM 内に収まる。Chapter 2 で数式の LaTeX 保持を確認済み。**採用** |

## 全章変換の実行方法

```bash
# Ollama 停止（VRAM 解放）
ollama stop qwen2.5:7b

# nohup で実行
cd ~/user/knowledge/hapke
nohup bash ./shell/shell.sh > shell/nohup.out 2>&1 &

# 進捗確認
tail -f shell/result.txt
```

`shell.sh` は変換済みの章（.md が存在する章）を自動スキップする。
VRAM 節約のため `--layout_batch_size 2 --recognition_batch_size 2 --equation_batch_size 2 --disable_multiprocessing` を指定している。

## 依存パッケージ

`pyproject.toml` に記載のもの + Marker 関連:

- marker-pdf 1.10.2（`uv pip install marker-pdf` で導入）
- torch 2.7.1+cu118（`--index-url https://download.pytorch.org/whl/cu118`）
- torchvision 0.22.1+cu118
- pymupdf, chromadb, rank-bm25, requests, gradio（pyproject.toml 管理）

## ライセンス・引用

対象書籍: Hapke, B. (2012). *Theory of Reflectance and Emittance Spectroscopy* (2nd ed.). Cambridge University Press.

本リポジトリは個人の研究用途でのみ使用する。PDF の再配布は行わない。
