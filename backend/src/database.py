import os
from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# .env を読み込む
load_dotenv()

# SQLite or PostgreSQL 切り替え
USE_SQLITE = os.getenv("USE_SQLITE", "false").lower() == "true"

if USE_SQLITE:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
    connect_args = {"check_same_thread": False}
else:
    # Docker/Poetry両対応のため、URLを .env に設定
    SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRES_URL")
    connect_args = {}

# エンジンとセッション
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
