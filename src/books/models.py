"""Database Representation of Application Memory data related to Book."""

import uuid
from datetime import UTC, date, datetime

import sqlalchemy.dialects.postgresql as pg
from pydantic_extra_types.language_code import LanguageName
from sqlmodel import Column, Field, SQLModel


class Book(SQLModel, table=True):
    """Book representation in database."""

    __tablename__ = "book"  # type: ignore

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: LanguageName
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

    def __repr__(self) -> str:
        """Return string representation of Book instance."""
        return f"<Book {self.title}>"
