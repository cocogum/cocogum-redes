from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import Role
from app.schemas.role import RoleCreate, RoleUpdate


async def get_role(db: AsyncSession, role_id: int):
    result = await db.execute(select(Role).filter(Role.id == role_id))
    return result.scalars().first()


async def get_roles(db: AsyncSession):
    result = await db.execute(select(Role))
    return result.scalars().all()


async def create_role(db: AsyncSession, role: RoleCreate):
    db_role = Role(**role.dict())
    db.add(db_role)
    await db.commit()
    await db.refresh(db_role)
    return db_role


async def update_role(db: AsyncSession, role_id: int, role: RoleUpdate):
    db_role = await get_role(db, role_id)
    for key, value in role.dict(exclude_unset=True).items():
        setattr(db_role, key, value)
    await db.commit()
    await db.refresh(db_role)
    return db_role


async def delete_role(db: AsyncSession, role_id: int):
    db_role = await get_role(db, role_id)
    await db.delete(db_role)
    await db.commit()
    return db_role
