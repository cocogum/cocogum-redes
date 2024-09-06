from datetime import datetime

import pytest
import pytz
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text  # Importar text

from app.db import get_async_session, get_engine
from app.main import app
from app.models import Role

# Crear una sesión asíncrona
async_session = sessionmaker(
    bind=get_engine(), class_=AsyncSession, expire_on_commit=False
)

# Constantes
HTTP_STATUS_OK = 200
TIME_ZONE = pytz.utc  # Definir la zona horaria


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://test') as ac:
        yield ac


@pytest.fixture
async def _setup_roles():
    async with get_async_session() as session:
        async with session.begin():
            now = datetime.now(TIME_ZONE)
            # Asegurarse de que 'now' tenga la zona horaria definida
            roles = [
                Role(name='admin1', created_at=now, updated_at=now),
                Role(name='Admin2', created_at=now, updated_at=now),
                Role(name='Admin3', created_at=now, updated_at=now),
                Role(name='Admin4', created_at=now, updated_at=now),
                Role(name='Visitante', created_at=now, updated_at=now),
                Role(name='Afiliado', created_at=now, updated_at=now),
                Role(name='Asociado', created_at=now, updated_at=now),
                Role(name='Socio', created_at=now, updated_at=now),
            ]
            await session.execute(text('DELETE FROM roles'))
            # Vaciar la tabla roles
            session.add_all(roles)
        await session.commit()


@pytest.mark.asyncio
@pytest.mark.usefixtures('_setup_roles')
async def test_read_root(client):
    response = await client.get('/')
    assert response.status_code == HTTP_STATUS_OK
    assert response.json() == {'message': 'Hello World'}


@pytest.mark.asyncio
@pytest.mark.usefixtures('_setup_roles')
async def test_example(client):
    response = await client.get('/some-endpoint')
    assert response.status_code == HTTP_STATUS_OK
    assert response.json() == {'message': 'success'}
