"""add content column to post table

Revision ID: 9cc3c6ff7d2e
Revises: 57b7e07d04c3
Create Date: 2024-06-06 11:09:30.204266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9cc3c6ff7d2e'
down_revision: Union[str, None] = '57b7e07d04c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
