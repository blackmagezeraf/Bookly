from datetime import UTC, datetime
from uuid import UUID, uuid4

import sqlalchemy.dialects.postgresql as pg
from pydantic import EmailStr
from sqlmodel import Column, Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"
    uid: UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid4)
    )
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    is_verfied: bool = Field(default=False)
    password_hash: str = Field(exclude=True)
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True), nullable=False, default=datetime.now(UTC)
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True), nullable=False, default=datetime.now(UTC)
        )
    )

    def __repr__(self):
        return f"<User {self.username}>"
