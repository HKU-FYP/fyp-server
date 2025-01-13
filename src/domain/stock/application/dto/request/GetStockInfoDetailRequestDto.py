from pydantic import BaseModel, Field


class GetStockInfoDetailRequestDto(BaseModel):
    ticker: str
