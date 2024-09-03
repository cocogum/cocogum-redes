import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Cargar las variables de entorno desde el archivo .env
load_dotenv()


class Settings(BaseSettings):
    app_name: str = 'My App'
    admin_email: str = 'admin@example.com'
    items_per_user: int = 50
    database_url: str = os.getenv('DATABASE_URL')


settings = Settings()
