import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text

from alembic import op

# revision identifiers, used by Alembic.
revision = 'fa0fe34c4501'
down_revision = '2315bc09a6b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Eliminar la tabla 'roles' si ya existe
    op.execute(text('DROP TABLE IF EXISTS roles CASCADE'))

    # Crear la tabla 'roles'
    op.create_table(
        'roles',
        sa.Column('id', sa.INTEGER(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.VARCHAR(), nullable=False, unique=True),
        sa.Column('created_at', postgresql.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(), nullable=False),
    )

    # Eliminar la tabla 'users' si ya existe
    op.execute(text('DROP TABLE IF EXISTS users CASCADE'))

    # Crear la tabla 'users'
    op.create_table(
        'users',
        sa.Column('id', sa.INTEGER(), primary_key=True, autoincrement=True),
        sa.Column('username', sa.VARCHAR(), nullable=True),
        sa.Column('email', sa.VARCHAR(), nullable=True),
        sa.Column('role', sa.INTEGER(), nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(), nullable=False),
        sa.Column('password', sa.VARCHAR(), nullable=False),
        sa.Column('person_id', sa.INTEGER(), nullable=True),
        sa.Column('First_name', sa.VARCHAR(length=120), nullable=False),
        sa.Column('Last_name', sa.VARCHAR(length=255), nullable=False),
    )

    # Eliminar la tabla 'users_role' si ya existe
    op.execute(text('DROP TABLE IF EXISTS users_role CASCADE'))

    # Crear la tabla 'users_role'
    op.create_table(
        'users_role',
        sa.Column('id', sa.INTEGER(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.INTEGER(), nullable=True),
        sa.Column('role_id', sa.INTEGER(), nullable=True),
        sa.Column('created_at', postgresql.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(), nullable=False),
        sa.ForeignKeyConstraint(
            ['role_id'], ['roles.id'], name='users_role_role_id_fkey'
        ),
        sa.ForeignKeyConstraint(
            ['user_id'], ['users.id'], name='users_role_user_id_fkey'
        ),
    )


def downgrade() -> None:
    op.drop_table('users_role')
    op.drop_table('roles')
    op.drop_table('users')
