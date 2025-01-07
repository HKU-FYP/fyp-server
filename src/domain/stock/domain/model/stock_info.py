from src.shared.database.connection import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import BigInteger, Boolean, DateTime, Integer, String

class StockInfo(Base):
    __tablename__ = 'stock_info'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ticker: Mapped[str] = mapped_column(String(500), nullable=False)
    name: Mapped[str] = mapped_column(String(500), nullable=False)