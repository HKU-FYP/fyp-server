from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import load_config

cfg = load_config()

MYSQL_DATABASE_URL = (
    f"mysql+pymysql://{cfg.db.username}:{cfg.db.password}@{cfg.db.host}:3306/{cfg.db.db_name}"
)
engine = create_engine(MYSQL_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("DB connection successful!")
Base = declarative_base()