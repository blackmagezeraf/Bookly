"""Fastapi Server entry point."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI

from src.books.routes import book_router
from src.config import Config
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI) -> AsyncGenerator[Any, Any]:
    """Server life span."""
    print("Server is starting...")
    await init_db()
    yield
    print("Server is Stopped...")


app = FastAPI(
    title="Bookly",
    description="Rest api for Book review web service",
    version=Config.VERSION,
    lifespan=life_span,
)

app.include_router(book_router, prefix=f"/api/{Config.VERSION}/books", tags=["books"])
