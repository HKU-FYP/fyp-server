from sqlalchemy import BigInteger, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from src.shared.database.connection import Base


class News(Base):
    __tablename__ = "news"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_stock_id: Mapped[int] = mapped_column(Integer, ForeignKey("user_stock.id"), nullable=False)

    title: Mapped[str] = mapped_column(String(500), nullable=False)
    author: Mapped[str] = mapped_column(String(500), nullable=True)

    published_date: Mapped[datetime.date] = mapped_column(DateTime, nullable=True)  # New column for publication date
    link: Mapped[str] = mapped_column(String(1000), nullable=True)  # New column for link
    publisher: Mapped[str] = mapped_column(String(500), nullable=True)  # New column for publisher
    content: Mapped[str] = mapped_column(Text, nullable=True)  # New column for long text content

    # System Generated
    summary: Mapped[str] = mapped_column(Text, nullable=True)
    sentiment: Mapped[str] = mapped_column(Text, nullable=True)
    sentiment_analysis: Mapped[str] = mapped_column(Text, nullable=True)
    stock_impact_analysis_easy: Mapped[str] = mapped_column(Text, nullable=True)
    stock_impact_analysis_intermediate: Mapped[str] = mapped_column(Text, nullable=True)
    stock_impact_analysis_expert: Mapped[str] = mapped_column(Text, nullable=True)

    # user = relationship("User")
    user_stock = relationship("UserStock")
