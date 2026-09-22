"""Book service layer."""

from datetime import UTC, datetime
from uuid import UUID

from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.books.models import Book as BookModel
from src.books.schemas import Book, BookCreateModel, BookUpdateModel


class BookService:
    """Book service layer."""

    async def _get_book_model(
        self, book_uid: UUID, session: AsyncSession
    ) -> BookModel | None:
        """Internal: retrieve ORM Model by UID.

        Args:
            book_uid (UUID): UUID of the book to get ORM Model of.
        """
        statement = select(BookModel).where(BookModel.uid == book_uid)
        result = await session.exec(statement)
        return result.first()

    async def get_all_books(self, session: AsyncSession) -> list[Book]:
        """Return all books ordered by creation date.

        Args:
            session (AsyncSession): The database session.
        """
        statement = select(BookModel).order_by(desc(BookModel.created_at))
        result = await session.exec(statement)
        return list(result.all())

    async def get_book(self, book_uid: UUID, session: AsyncSession) -> Book | None:
        """Return a book by its ID.

        Args:
            book_uid (UUID): The ID of the book to retrieve.
            session (AsyncSession): The database session.
        """
        return await self._get_book_model(book_uid, session)

    async def create_book(
        self, book_data: BookCreateModel, session: AsyncSession
    ) -> Book:
        """Create a new book.

        Args:
            book_data (BookCreateMode): Data that the new book will be holding.
            session (AsyncSession): The database session.
        """
        book_data_dict = book_data.model_dump()
        new_book = BookModel(**book_data_dict)
        new_book.published_date = datetime.now(UTC)
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book

    async def update_book(
        self, book_uid: UUID, book_data: BookUpdateModel, session: AsyncSession
    ) -> Book | None:
        """Update a book by its ID.

        Args:
            book_uid (UUID): UID of the book to update.
            book_data (BookCreateMode): Data that the updated book will be holding.
            session (AsyncSession): The database session.
        """
        book_to_update = await self.get_book(book_uid, session)

        if book_to_update is not None:
            book_update_dict = book_data.model_dump(exclude_unset=True)

            for key, value in book_update_dict.items():
                setattr(book_to_update, key, value)

            book_data.updated_at = datetime.now(UTC)

            session.add(book_to_update)
            await session.commit()
            await session.refresh(book_to_update)
            return book_to_update

        return None

    async def delete_book(self, book_uid: UUID, session: AsyncSession) -> Book | None:
        """Delete a book by its ID.

        Args:
            book_uid (UUID): UID of the book to delete.
            session (AsyncSession): The database session.
        """
        book_to_delete = await self.get_book(book_uid, session)

        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            return book_to_delete

        return None
