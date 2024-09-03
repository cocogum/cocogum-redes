# init_db.py
import asyncio
from datetime import datetime, timezone
from app.models.role import Role
from app.database import SessionLocal, create_db_and_tables

async def init_db():
    async with SessionLocal() as session:
        roles = [
            "admin1", "Admin2", "Admin3", "Admin4",
            "Visitante", "Afiliado", "Asociado", "Socio"
        ]
        for role_name in roles:
            now = datetime.now(timezone.utc)
            role = Role(name=role_name, created_at=now, updated_at=now)
            session.add(role)
        await session.commit()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(create_db_and_tables())
    loop.run_until_complete(init_db())
    loop.close()