"""add content column to posts table

Revision ID: bb534734ba76
Revises: bee8cb3c08ea
Create Date: 2022-04-19 09:17:34.119621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb534734ba76'
down_revision = 'bee8cb3c08ea'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
