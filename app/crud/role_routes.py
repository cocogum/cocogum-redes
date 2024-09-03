from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_current_user
from app.crud import role as role_crud
from app.database import get_db
from app.schemas.role import Role, RoleCreate, RoleUpdate
from app.schemas.user import User

router = APIRouter()


@router.post('/roles/', response_model=Role)
async def create_role(
    role: RoleCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await role_crud.create_role(db=db, role=role)


@router.get('/roles/', response_model=List[Role])
async def get_roles(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await role_crud.get_roles(db=db)


@router.put('/roles/{role_id}', response_model=Role)
async def update_role(
    role_id: int,
    role: RoleUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_role = await role_crud.get_role(db, role_id=role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail='Role not found')
    return await role_crud.update_role(db=db, role_id=role_id, role=role)


@router.delete('/roles/{role_id}', response_model=Role)
async def delete_role(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_role = await role_crud.get_role(db, role_id=role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail='Role not found')
    return await role_crud.delete_role(db=db, role_id=role_id)
