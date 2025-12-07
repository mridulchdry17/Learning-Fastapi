from sqlmodel import create_engine,text
from src.config import Config
from sqlalchemy.ext.asyncio import AsyncEngine
from src.books.models import Book
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

engine = AsyncEngine(create_engine(
    url = Config.DATABASE_URL,
    echo = True
))


async def initdb():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        bind = engine,class_= AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session   