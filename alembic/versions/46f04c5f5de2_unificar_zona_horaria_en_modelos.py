"""Unificar zona horaria en modelos

Revision ID: 46f04c5f5de2
Revises: 6ee18f4f392b
Create Date: 2024-09-05 15:12:59.810159

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46f04c5f5de2'
down_revision: Union[str, None] = '6ee18f4f392b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass