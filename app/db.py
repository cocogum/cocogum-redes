import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Crear el motor asíncrono
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear una sesión asíncrona
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


def get_engine():
    return engine


def get_async_session():
    return async_session()
