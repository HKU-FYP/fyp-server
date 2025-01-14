from sqlalchemy import BigInteger, ForeignKey, Integer, String, Date, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from src.shared.database.connection import Base

class News(Base):
    __tablename__ = 'news'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    user_stock_id: Mapped[int] = mapped_column(Integer, ForeignKey("user_stock.id"), nullable=False)

    title: Mapped[str] = mapped_column(String(500), nullable=False)
    author: Mapped[str] = mapped_column(String(500), nullable=True)

    published_date: Mapped[datetime.date] = mapped_column(Date, nullable=True)  # New column for publication date
    link: Mapped[str] = mapped_column(String(1000), nullable=True)             # New column for link
    publisher: Mapped[str] = mapped_column(String(500), nullable=True)         # New column for publisher
    content: Mapped[str] = mapped_column(Text, nullable=True)                  # New column for long text content

    user = relationship("User")
    user_stock = relationship("UserStock")
