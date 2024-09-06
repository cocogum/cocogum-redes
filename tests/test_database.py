import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import create_db_and_tables, get_db


@pytest_asyncio.fixture
async def test_create_db_and_tables():
    await create_db_and_tables()
    async for session in get_db():
        assert isinstance(session, AsyncSession)
