from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.user import create_user, get_user, get_user_by_email
from app.database import get_db
from app.schemas.user import User as UserSchema
from app.schemas.user import UserCreate

user_router = APIRouter()


@user_router.post('/users/', response_model=UserSchema)
async def create_new_user(
    user: UserCreate, db: AsyncSession = Depends(get_db)
):
    db_user = await get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return await create_user(db, user)


@user_router.get('/users/{user_id}', response_model=UserSchema)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user
