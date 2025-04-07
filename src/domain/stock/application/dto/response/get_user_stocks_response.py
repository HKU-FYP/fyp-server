from pydantic import BaseModel, Field


class UserStockInfoDto(BaseModel):
    id: int = Field(...)
    user_stock_id: int = Field(...)
    ticker: str = Field(...)
    name: str = Field(...)
