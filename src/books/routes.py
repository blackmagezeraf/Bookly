"""Book API Routes."""

from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from sqlmodel.ext.asyncio.session import AsyncSession

from src.books.service import BookService
from src.db.main import get_session

from .models import Book
from .schemas import BookCreateModel, BookUpdateModel

book_router = APIRouter()
book_service = BookService()


@book_router.get("/", response_model=list[Book])
async def get_books(session: AsyncSession = Depends(get_session)) -> list[Book]:  # noqa: B008
    """Get all the Books.

    Args:
        session: Async database session.
    """
    return await book_service.get_all_books(session)


@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(
    book_data: BookCreateModel,
    session: AsyncSession = Depends(get_session),  # noqa: B008
) -> Book:
    """Create and add a new Book.

    Args:
        book_data: Data for the new book.
        session: Async database session.
    """
    return await book_service.create_book(book_data, session)


@book_router.get("/{book_uid}")
async def get_book(
    book_uid: UUID,
    session: AsyncSession = Depends(get_session),  # noqa: B008
) -> Book:
    """Find the book with specific ID.

    Args:
        book_uid: UUID of the book in DB you are looking for.
        session: Async database session.
    """
    book = await book_service.get_book(book_uid, session)
    if book is not None:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")


@book_router.patch("/{book_uid}")
async def update_book(
    book_uid: UUID,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),  # noqa: B008
) -> Book:
    """Update an existing book record partially or fully.

    Args:
        book_uid: UUID of the book to update.
        book_update_data: Fields to update in the book.
        session: Async database session.
    """
    updated_book = await book_service.update_book(book_uid, book_update_data, session)
    if updated_book is not None:
        return updated_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book record not found.")


@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book_uid: UUID,
    session: AsyncSession = Depends(get_session),  # noqa: B008
) -> None:
    """Delete the book if the ID matches.

    Args:
        book_uid: Book UUID to delete.
        session: Async database session.
    """
    book = await book_service.delete_book(book_uid, session)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book record not found")
