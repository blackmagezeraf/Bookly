from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.auth.models import User
from src.auth.schemas import UserCreateModel
from src.auth.utils import generate_password_hash


class UserService:
    """Service for managing users."""

    async def get_user_by_email(self, email: str, session: AsyncSession) -> User | None:
        """Get the user by Email.

        Args:
            email (str): email to get user by.
            session (AsyncSession): Current Database session.
        """
        statement = select(User).where(User.email == email)
        result = await session.exec(statement)
        return result.first()

    async def user_exists(self, email: str, session: AsyncSession) -> bool:
        """If User Exists returns True else False."""
        user = await self.get_user_by_email(email=email, session=session)
        return user is not None

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession) -> User:
        """Create a new user if doesn't exist.

        Args:
            user_data (UserCreateModel): New user data
            session (AsyncSession): current database session
        """
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        new_user.password_hash = generate_password_hash(user_data_dict["password"])
        session.add(new_user)
        await session.commit()
        await session.refresh(instance=new_user)
        return new_user
