from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.shared.database.connection import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    # embedding_threshold: Mapped[float] = mapped_column(Float, nullable=False, default=0.3)
    username: Mapped[str] = mapped_column(String(500), nullable=False)
    password: Mapped[str] = mapped_column(String(500), nullable=False)
