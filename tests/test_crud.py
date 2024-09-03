# tests/test_crud.py
import pytest
from sqlalchemy.orm import Session
from app.crud import user as crud_user
from app.schemas.user import UserCreate

def test_create_user(db_session: Session):
    user_in = UserCreate(username="testuser", email="testuser@example.com", password="password")
    user = crud_user.create_user(db=db_session, user=user_in)
    assert user.id is not None
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"