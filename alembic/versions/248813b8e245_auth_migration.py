"""Auth migration

Revision ID: 248813b8e245
Revises: 46f04c5f5de2
Create Date: 2024-09-05 16:26:54.495089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '248813b8e245'
down_revision: Union[str, None] = '46f04c5f5de2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
