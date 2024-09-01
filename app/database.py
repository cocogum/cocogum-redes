from sqlmodel import SQLModel, create_engine, Session
from .config import settings

# Crear el motor de la base de datos
engine = create_engine(settings.database_url)

# Crear todas las tablas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    with Session(engine) as session:
        yield session