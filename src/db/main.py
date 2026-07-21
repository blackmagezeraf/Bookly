"""Database Initialization and setup."""

from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import create_engine

from src.books.models import Book
from src.config import Config

engine = AsyncEngine(create_engine(url=Config.DATABASE_URL, echo=True))


async def init_db() -> None:
    """Initialize Database."""
    async with engine.begin() as db_connection:
        await db_connection.run_sync(Book.metadata.create_all)
