from pydantic import BaseModel, Field

class SignUpRequestDto(BaseModel):
    username: str = Field(...)
    password: str = Field(...)