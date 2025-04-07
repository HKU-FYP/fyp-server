import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv
from openai import OpenAI


@dataclass
class OpenAIConfig:
    api_key: str
    embedding_model: str
    chat_model: str


@dataclass
class DBConfig:
    host: str
    db_name: str
    username: str
    password: str


@dataclass
class JwtConfig:
    secret_key: str


@dataclass
class StockAPIConfig:
    api_key: str

@dataclass
class DiscordConfig:
    channel_id: str
    bot_token: str


@dataclass
class AppConfig:
    db: DBConfig
    openai: OpenAIConfig
    jwt: JwtConfig
    stock: StockAPIConfig
    discord: DiscordConfig


@lru_cache
def load_config() -> AppConfig:
    # load_dotenv(".env", override=True)
    load_dotenv()

    os.environ["MYSQL_HOST"] = "127.0.0.1"
    os.environ["MYSQL_USER"] = "root"
    os.environ["MYSQL_PASSWORD"] = "1234qwer"
    os.environ["MYSQL_DB_NAME"] = "fyp"
    os.environ["JWT_SECRET_KEY"] = "sample-secret-key"

    db_config = DBConfig(
        host=os.environ["MYSQL_HOST"],
        username=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        db_name=os.environ["MYSQL_DB_NAME"],
    )

    openai_config = OpenAIConfig(
        api_key=os.environ["OPENAI_API_KEY"], embedding_model="text-embedding-ada-002", chat_model="gpt-4o-mini"
    )

    discord_config = DiscordConfig(os.environ["DISCORD_CHANNEL_ID"], os.environ["DISCORD_BOT_TOKEN"])

    jwt_config = JwtConfig(secret_key=os.environ["JWT_SECRET_KEY"])
    stock_config = StockAPIConfig(api_key=os.environ["TWELVE_API_KEY"])
    return AppConfig(db=db_config, openai=openai_config, jwt=jwt_config, stock=stock_config, discord=discord_config)
