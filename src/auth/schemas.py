from pydantic import BaseModel, EmailStr, Field


class UserCreateModel(BaseModel):
    username: str = Field(max_length=8)
    email: EmailStr = Field(max_length=40)
    password: str = Field(min_length=6)
