# tests/test_models.py
from sqlalchemy.orm import Session

from app.models import Role, User


def test_create_user(db_session: Session):
    user = User(username='testuser', email='testuser@example.com')
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    assert user.id is not None
    assert user.username == 'testuser'
    assert user.email == 'testuser@example.com'


def test_create_role(db_session: Session):
    role = Role(name='admin')
    db_session.add(role)
    db_session.commit()
    db_session.refresh(role)
    assert role.id is not None
    assert role.name == 'admin'


def test_roles_exist(db_session: Session):
    roles = db_session.query(Role).all()
    role_names = [role.name for role in roles]
    expected_roles = [
        'admin1',
        'Admin2',
        'Admin3',
        'Admin4',
        'Visitante',
        'Afiliado',
        'Asociado',
        'Socio',
    ]
    for role in expected_roles:
        assert role in role_names
