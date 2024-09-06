from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.role import create_role, get_role
from app.database import get_db
from app.schemas.role import Role as RoleSchema
from app.schemas.role import RoleCreate

role_router = APIRouter()


@role_router.post('/roles/', response_model=RoleSchema)
async def create_new_role(
    role: RoleCreate, db: AsyncSession = Depends(get_db)
):
    return await create_role(db, role)


@role_router.get('/roles/{role_id}', response_model=RoleSchema)
async def read_role(role_id: int, db: AsyncSession = Depends(get_db)):
    db_role = await get_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail='Role not found')
    return db_role
