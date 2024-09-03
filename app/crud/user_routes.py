from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_current_user
from app.crud import user as user_crud
from app.database import get_db
from app.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()


@router.post('/users/', response_model=User)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_user = await user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return await user_crud.create_user(db=db, user=user)


@router.put('/users/{user_id}', response_model=User)
async def update_user(
    user_id: int,
    user: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_user = await user_crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    return await user_crud.update_user(db=db, user_id=user_id, user=user)


@router.delete('/users/{user_id}', response_model=User)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_user = await user_crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    return await user_crud.delete_user(db=db, user_id=user_id)
