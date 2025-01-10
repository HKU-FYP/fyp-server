from sqlalchemy import Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.shared.database.connection import Base

class UserStock(Base):
    __tablename__ = "user_stock"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    stock_info_id: Mapped[int] = mapped_column(Integer, ForeignKey('stock_info.id'), nullable=False)

    user = relationship("User")
    stock_info = relationship("StockInfo")