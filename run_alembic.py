import os
import sys

from dotenv import load_dotenv

from alembic.config import CommandLine

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Ejecutar Alembic
alembic = CommandLine()
alembic.main()
