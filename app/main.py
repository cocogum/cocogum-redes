from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import create_db_and_tables
from app.routers.auth import auth_router
from app.routers.role import role_router
from app.routers.user import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código de inicio
    await create_db_and_tables()
    yield
    # Código de cierre
    # Código de limpieza


app = FastAPI(lifespan=lifespan)


# Ruta para la raíz
@app.get('/')
async def read_root():
    return {'message': 'Hello World'}


# Añadir el endpoint /some-endpoint
@app.get('/some-endpoint')
async def some_endpoint():
    return {'message': 'success'}


app.include_router(user_router, prefix='/api/v1', tags=['users'])
app.include_router(role_router, prefix='/api/v1', tags=['roles'])
app.include_router(auth_router, prefix='/api/v1', tags=['auth'])
