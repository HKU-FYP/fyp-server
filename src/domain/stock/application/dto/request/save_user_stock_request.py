from pydantic import BaseModel, Field


class SaveUserStockRequestDto(BaseModel):
    stock_info_id: list[int] = Field(...)
