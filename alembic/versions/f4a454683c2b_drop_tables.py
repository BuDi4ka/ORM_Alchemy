"""drop tables

Revision ID: f4a454683c2b
Revises: f0b53b64c7a7
Create Date: 2024-10-07 12:13:21.153291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4a454683c2b'
down_revision: Union[str, None] = 'f0b53b64c7a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('TRUNCATE TABLE grades RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE students RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE subjects RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE teachers RESTART IDENTITY CASCADE;')
    op.execute('TRUNCATE TABLE groups RESTART IDENTITY CASCADE;')


def downgrade() -> None:
    pass
