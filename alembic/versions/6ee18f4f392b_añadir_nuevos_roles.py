"""Añadir nuevos roles

Revision ID: 6ee18f4f392b
Revises: fa0fe34c4501
Create Date: 2024-09-05 08:21:47.388022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ee18f4f392b'
down_revision: Union[str, None] = 'fa0fe34c4501'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
