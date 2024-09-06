from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.auth import authenticate_user
from app.database import get_db
from app.schemas.auth import AuthDetails

auth_router = APIRouter()


@auth_router.post('/auth/', response_model=AuthDetails)
async def login(auth_details: AuthDetails, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, auth_details)
    if not user:
        raise HTTPException(status_code=400, detail='Invalid credentials')
    return user
