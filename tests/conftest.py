import asyncio
from datetime import datetime

import pytest
import pytest_asyncio
import pytz
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text  # Importar text

from app.config import settings  # Importar la configuración
from app.models.base import Base
from app.models.role import Role  # Asegúrate de importar el modelo Role

# Definir la zona horaria
TIME_ZONE = pytz.utc

# Definir la longitud mínima del nombre del rol
MIN_ROLE_NAME_LENGTH = 5

DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='function', autouse=True)
async def db_engine():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all, checkfirst=True)


@pytest_asyncio.fixture
def db_session_factory(db_engine):
    return sessionmaker(
        autocommit=False, autoflush=False, bind=db_engine, class_=AsyncSession
    )


@pytest_asyncio.fixture
async def db_session(db_session_factory):
    async with db_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()


@pytest_asyncio.fixture
async def setup_roles(db_session):
    roles = [
        'admin1',
        'Admin2',
        'Admin3',
        'Admin4',
        'Visitante',
        'Afiliado',
        'Asociado',
        'Socio',
    ]

    # Vaciar la tabla roles
    await db_session.execute(text('DELETE FROM roles'))
    await db_session.commit()

    for role_name in roles:
        # Validar longitud mínima
        if len(role_name) < MIN_ROLE_NAME_LENGTH:
            raise ValueError(
                f"El nombre del rol '{role_name}' es demasiado corto. "
                f'Debe tener al menos {MIN_ROLE_NAME_LENGTH} caracteres.'
            )

        # Obtener el datetime actual con zona horaria UTC
        aware_datetime = datetime.now(TIME_ZONE)

        role = Role(
            name=role_name,
            created_at=aware_datetime,
            updated_at=aware_datetime,
        )
        db_session.add(role)
    await db_session.commit()
