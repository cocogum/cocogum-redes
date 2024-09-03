from fastapi import FastAPI

from app.auth import router as auth_router
from app.crud.role_routes import router as role_router
from app.crud.user_routes import router as user_router
from app.database import create_db_and_tables

app = FastAPI()


@app.on_event('startup')
async def on_startup():
    await create_db_and_tables()


# Ruta para la raíz
@app.get('/')
async def read_root():
    return {'message': 'Hello World'}


# Ruta para items
@app.get('/items/')
async def read_items():
    return [{'item_id': 1, 'name': 'Item 1'}, {'item_id': 2, 'name': 'Item 2'}]


app.include_router(user_router, prefix='/api/v1', tags=['users'])
app.include_router(role_router, prefix='/api/v1', tags=['roles'])
app.include_router(auth_router, prefix='/api/v1', tags=['auth'])
