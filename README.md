# Portfolio Auto Generator

ポートフォリオを自動生成する Web アプリケーションです。

## 機能

- 名前、自己紹介、スキルの入力フォーム
- 入力された情報を基にポートフォリオページを自動生成
- レスポンシブな Web デザイン

## 技術スタック

- **Backend**: FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **Template Engine**: Jinja2

## 必要な環境

- Python 3.7 以上
- pip

## インストール・実行手順

### 1. リポジトリをクローン

```bash
git clone <リポジトリURL>
cd portfolio-auto
```

### 2. 仮想環境の作成と有効化

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
```

### 3. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 4. アプリケーションの起動

```bash
uvicorn app.main:app --reload
```

### 5. ブラウザでアクセス

アプリケーションが起動したら、ブラウザで以下の URL にアクセスしてください：

```
http://localhost:8000
```
