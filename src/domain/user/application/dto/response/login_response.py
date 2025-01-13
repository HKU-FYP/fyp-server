from pydantic import BaseModel, Field


class LoginResponseDto(BaseModel):
    access_token: str = Field(...)
