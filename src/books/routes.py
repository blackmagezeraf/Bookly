from typing import Any

from fastapi import HTTPException, status
from fastapi.routing import APIRouter

from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel

book_router = APIRouter()


@book_router.get("/", response_model=list[Book])
async def get_books() -> list[dict[str, Any]]:
    """Get all the Books."""
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book) -> dict[str, Any]:
    """Create and add a new Book."""
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@book_router.get("/{book_id}")
async def get_book(book_id: int) -> dict[str, Any]:
    """
    Find the book with specific ID

    Args:
        book_id -> int:
            `id` of the book in DB you are looking for.
    """
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book not found."
    )


@book_router.patch("/{book_id}")
async def update_book(
    book_id: int, book_update_data: BookUpdateModel
) -> dict[str, Any]:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["published_date"] = book_update_data.published_date
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book record not found."
    )


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int) -> None:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book record not found"
    )
