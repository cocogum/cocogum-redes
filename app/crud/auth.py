from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.security import verify_password
from app.models.user import User
from app.schemas.auth import AuthDetails


async def authenticate_user(
    db: AsyncSession, auth_details: AuthDetails
) -> User:
    result = await db.execute(
        select(User).filter(User.username == auth_details.username)
    )
    user = result.scalars().first()
    if user and verify_password(auth_details.password, user.hashed_password):
        return user
    return None
