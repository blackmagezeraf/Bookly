"""Routes of all the authentication related."""

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from src.auth.schemas import UserCreateModel, UserModel
from src.auth.service import UserService
from src.db.main import get_session

auth_router = APIRouter()
user_service = UserService()


@auth_router.get("/signup", response_model=UserModel)
async def create_user_account(
    user_data: UserCreateModel, session: AsyncSession = Depends(get_session)
):
    """Create a new user account.

    Args:
        user_data (UserCreateModel): The user data to create the account with.
        session (AsyncSession): The database session.
    """
    email = user_data.email
    user_exists = await user_service.user_exists(email, session)

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User email already exists"
        )

    await user_service.create_user(user_data, session)
