from datetime import UTC, datetime
from uuid import UUID, uuid4

import sqlalchemy.dialects.postgresql as pg
from pydantic import EmailStr
from sqlmodel import Column, Field, SQLModel


class User(SQLModel, table=True):  # type: ignore
    __tablename__ = "users"  # type: ignore
    uid: UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid4)  # type: ignore
    )
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    is_verfied: bool = Field(default=False)  # type: ignore
    password_hash: str = Field(exclude=True)  # type: ignore
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP(timezone=True), nullable=False, default=datetime.now(UTC)))  # type: ignore
    updated_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP(timezone=True), nullable=False, default=datetime.now(UTC)))  # type: ignore

    def __repr__(self):
        return f"<User {self.username}>"
