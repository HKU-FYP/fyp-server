from sqlalchemy import BigInteger, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from src.shared.database.connection import Base

class Metric(Base):
    __tablename__ = "metric"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    news_id: Mapped[int] = mapped_column(Integer, ForeignKey("news.id"), nullable=False)
    metric_content: Mapped[str] = mapped_column(String(500), nullable=False)

    news = relationship("News")

