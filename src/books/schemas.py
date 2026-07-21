"""Book related Data Representation in application memory."""

from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel
from pydantic_extra_types.language_code import LanguageName


class Book(BaseModel):
    """Book listing data structure representation in memory."""

    uid: UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: LanguageName
    created_at: datetime
    updated_at: datetime


class BookCreateModel(BaseModel):
    """Book Creation data structure representation in memory."""

    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: LanguageName


class BookUpdateModel(BaseModel):
    """Book Updation data structure representation in memory."""

    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: LanguageName
    created_at: datetime
    updated_at: datetime
