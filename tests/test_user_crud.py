import pytest_asyncio

from app.models.user import User


@pytest_asyncio.fixture
async def test_create_user(db_session):
    new_user = User(
        email='test@example.com',
        username='testuser',
        first_name='Test',
        last_name='User',
        phone='1234567890',
        hashed_password='hashedpassword',
    )
    db_session.add(new_user)
    await db_session.commit()
    assert new_user.id is not None


@pytest_asyncio.fixture
async def test_get_user(db_session):
    result = await db_session.execute(
        "SELECT * FROM users WHERE email='test@example.com'"
    )
    user = result.fetchone()
    assert user is not None


@pytest_asyncio.fixture
async def test_get_user_by_email(db_session):
    result = await db_session.execute(
        "SELECT * FROM users WHERE email='test@example.com'"
    )
    user = result.fetchone()
    assert user is not None


@pytest_asyncio.fixture
async def test_update_user(db_session):
    result = await db_session.execute(
        "SELECT * FROM users WHERE email='test@example.com'"
    )
    user = result.fetchone()
    user.first_name = 'Updated'
    await db_session.commit()
    assert user.first_name == 'Updated'


@pytest_asyncio.fixture
async def test_delete_user(db_session):
    result = await db_session.execute(
        "SELECT * FROM users WHERE email='test@example.com'"
    )
    user = result.fetchone()
    await db_session.delete(user)
    await db_session.commit()
    result = await db_session.execute(
        "SELECT * FROM users WHERE email='test@example.com'"
    )
    user = result.fetchone()
    assert user is None
