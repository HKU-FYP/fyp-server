import os
from dataclasses import dataclass
from dotenv import load_dotenv
from functools import lru_cache

@dataclass
class DBConfig:
    host: str
    db_name: str
    username: str
    password: str

@dataclass
class AppConfig:
    db: DBConfig


@lru_cache
def load_config() -> AppConfig:
    load_dotenv('.env', override=True)
    os.environ['MYSQL_HOST'] = '127.0.0.1'
    os.environ['MYSQL_USER'] = 'root'
    os.environ['MYSQL_PASSWORD'] = '1234qwer'
    os.environ['MYSQL_DB_NAME'] = 'fyp'

    db_config = DBConfig(
        host=os.environ["MYSQL_HOST"],
        username=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        db_name=os.environ["MYSQL_DB_NAME"],
    )
    return AppConfig(db=db_config)