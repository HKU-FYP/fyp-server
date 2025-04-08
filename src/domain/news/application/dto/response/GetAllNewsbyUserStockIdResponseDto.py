from pydantic import BaseModel, Field
from datetime import datetime


class GetAllNewsByUserStockIdResponseDto(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    author: str = Field(...)
    published_date: datetime = Field(...)
    link: str = Field(...)
    publisher: str = Field(...)
    content: str = Field(...)
    sentiment: str = Field(...)
    one_sentence_summary: str = Field(...)
