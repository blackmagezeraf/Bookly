import uuid
from datetime import datetime

import sqlalchemy.dialects.postgresql as pg
from pydantic_extra_types.language_code import LanguageName
from sqlmodel import Column, Field, SQLModel


class Book(SQLModel, table=True):
    __tablename__ = "book"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4()
        )
    )
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    langauge: LanguageName
    created_at: datetime = Field(Column(pg.TIMESTAMP, default=datetime.now()))
    updated_at: datetime = Field(Column(pg.TIMESTAMP, default=datetime.now()))
