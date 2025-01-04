from pydantic import BaseModel, Field


class GetSampleResponseDto(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    description: str = Field(...)
