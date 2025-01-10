from pydantic import BaseModel, Field


class SignUpResponseDto(BaseModel):
    user_id: int = Field(...)
