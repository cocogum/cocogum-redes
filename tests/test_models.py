import pytest_asyncio

from app.models.role import Role
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
async def test_create_role(db_session):
    new_role = Role(name='Test Role')
    db_session.add(new_role)
    await db_session.commit()
    assert new_role.id is not None


@pytest_asyncio.fixture
async def test_roles_exist(db_session):
    result = await db_session.execute('SELECT * FROM roles')
    roles = result.fetchall()
    assert roles is not None
