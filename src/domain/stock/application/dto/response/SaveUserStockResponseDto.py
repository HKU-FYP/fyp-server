from pydantic import BaseModel, Field


class SaveUserStockResponseDto(BaseModel):
    user_stock_id: int = Field(...)
