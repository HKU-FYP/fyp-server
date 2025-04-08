from pydantic import BaseModel, Field


class SaveUserStockResponseDto(BaseModel):
    user_stock_id: list[int] = Field(...)
