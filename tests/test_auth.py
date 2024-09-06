import pytest
from fastapi import HTTPException
import jwt
from app.auth.utils import create_access_token, verify_token

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
USER_ID = 123  # Mantener como entero

def test_create_access_token():
    data = {'sub': str(USER_ID)}  # Convertir a cadena
    token = create_access_token(data)
    assert token is not None

    # Decodificar el token para verificar su contenido
    decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded_data['sub'] == str(USER_ID)  # Comparar con una cadena
    assert 'exp' in decoded_data

def test_verify_token():
    data = {'sub': str(USER_ID)}  # Convertir a cadena
    token = create_access_token(data)
    user_id = verify_token(token)
    assert user_id == str(USER_ID)  # Comparar con una cadena

def test_verify_token_invalid():
    with pytest.raises(HTTPException, match='Could not validate credentials'):
        verify_token('invalid_token')