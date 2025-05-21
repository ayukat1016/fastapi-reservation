# udemy-fastapi-reservation

Docker環境とPoetry仮想環境の実行方法を記載

## Docker環境実行
### 環境変数
`frontend`と`backend`の`src/.env`の環境変数を設定
する
#### バックエンド
```sh
# postgresを使わないときはtrueを指定
USE_SQLITE=false
```
#### フロントエンド
```sh
# docker-compose.yamlのサービス名を指定
BACKEND_URL=http://backend:8000
```

### 環境構築

#### ライブラリ変更時
```sh
poetry export --without-hashes -f requirements.txt --output requirements.txt
```

#### コードやライブラリの変更発生時
```sh
docker compose build
```

### 実行方法
#### コンテナ起動
```sh
docker compose up -d
```

#### コンテナ停止
```sh
docker compose down
```

#### DB操作
```sh
docker exec -it postgres bash
# password　と入力
root@postgres:/# psql -U postgres reservation -W
```

## Poetry仮想環境実行

### 環境変数
`frontend`と`backend`の`src/.env`の環境変数を設定
する
#### バックエンド
```sh
USE_SQLITE=true
```
#### フロントエンド
```sh
BACKEND_URL=http://localhost:8000
```

### 環境構築
新しいディレクトリを使用するとき`frontend`と`backend`のディレクトリで仮想環境を構築する
```sh
pyenv local 3.9.13
poetry install
```

### 実行方法

#### バックエンド
```sh
poetry run uvicorn src.main:app --reload
```

#### フロントエンド
```sh
poetry run streamlit run src/main.py
```