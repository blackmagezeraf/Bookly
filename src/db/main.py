from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import create_engine, text

from src.config import Config

engine = AsyncEngine(create_engine(url=Config.DATABASE_URL, echo=True))


async def init_db():
    async with engine.begin() as db_connection:
        statement = text("SELECT 'hello';")

        result = await db_connection.execute(statement)

        print(result.all())
