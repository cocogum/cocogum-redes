import os

from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde el archivo .env


class Settings:
    DATABASE_URL: str = os.getenv('DATABASE_URL')


settings = Settings()
