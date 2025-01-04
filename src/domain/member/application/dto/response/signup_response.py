from pydantic import BaseModel, Field


class SignUpResponseDto(BaseModel):
    member_id: int = Field(...)
