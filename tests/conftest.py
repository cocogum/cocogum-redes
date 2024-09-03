# tests/conftest.py

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.base import Base
from app.models.role import Role

load_dotenv()


@pytest.fixture(scope='session')
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(bind=engine)
    return engine


@pytest.fixture(scope='session')
def db_session_factory(db_engine):
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=db_engine
    )
    return TestingSessionLocal


@pytest.fixture
def db_session(db_session_factory):
    session = db_session_factory()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture(scope='session', autouse=True)
def _setup_roles(db_session_factory):
    session = db_session_factory()
    roles = [
        'admin1',
        'Admin2',
        'Admin3',
        'Admin4',
        'Visitante',
        'Afiliado',
        'Asociado',
        'Socio',
    ]
    for role_name in roles:
        role = Role(name=role_name)
        session.add(role)
    session.commit()
    session.close()
