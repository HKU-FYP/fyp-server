from pydantic import BaseModel, Field

class EmbeddingSearchResponseDto(BaseModel):
    tickers: list[str]