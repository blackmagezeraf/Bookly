from pydantic import BaseModel, EmailStr, Field


class UserCreateModel(BaseModel):
    """Represents a user creation request."""
    username: str = Field(max_length=8)  # type: ignore
    email: EmailStr = Field(max_length=40)  # type: ignore
    password: str = Field(min_length=6)  # type: ignore


class UserModel(BaseModel):
    """Represents a user in the system."""
    pass
