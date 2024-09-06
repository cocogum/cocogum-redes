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
