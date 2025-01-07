from pydantic import BaseModel, Field

class StockInfoDto(BaseModel):
    id: int = Field(...)
    ticker: str = Field(...)
    name: str = Field(...)

class GetStockInfoResponseDto(BaseModel):
    stocks: list[StockInfoDto] = Field(...)