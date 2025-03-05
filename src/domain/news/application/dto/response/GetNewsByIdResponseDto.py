from pydantic import BaseModel, Field
from datetime import datetime

class GetNewsByIdResponseDto(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    author: str = Field(...)

    published_date: datetime = Field(...)
    link: str = Field(...)
    publisher: str = Field(...)
    content: str = Field(...)

    summary: str = Field(...)
    sentiment: str = Field(...)
    sentiment_analysis: str = Field(...)
    stock_impact_analysis_easy: str = Field(...)
    stock_impact_analysis_intermediate: str = Field(...)
    stock_impact_analysis_expert: str = Field(...)

    key_metrics: list[str] = Field(...)
