"""Routes of all the authentication related."""

from fastapi import APIRouter

from src.auth.schemas import UserCreateModel

auth_router = APIRouter()


@auth_router.get("/signup")
async def create_user_account(user_data: UserCreateModel):
    pass
