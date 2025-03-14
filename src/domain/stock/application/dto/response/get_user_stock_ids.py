from pydantic import BaseModel, Field

class GetUserStockIdResponse(BaseModel):
    userStockId: int = Field(...)