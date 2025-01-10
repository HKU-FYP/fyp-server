from pydantic import BaseModel, Field


class CheckUserStockExistResponseDto(BaseModel):
    exist: bool = Field(...)