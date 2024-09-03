import pytest
from httpx import AsyncClient

from app.main import app

# Definir una constante para el código de estado HTTP 200
HTTP_STATUS_OK = 200


@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get('/')
    assert response.status_code == HTTP_STATUS_OK
    assert response.json() == {'message': 'Hello World'}


@pytest.mark.asyncio
async def test_read_items():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get('/items/')
    assert response.status_code == HTTP_STATUS_OK
    assert isinstance(response.json(), list)
