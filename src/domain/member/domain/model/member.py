from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.shared.database.connection import Base


class Member(Base):
    __tablename__ = "member"

    id: Mapped[str] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username: Mapped[str] = mapped_column(String(500), nullable=False)
    password: Mapped[str] = mapped_column(String(500), nullable=False)