"""add all columns to posts table

Revision ID: 8366fec7806d
Revises: 4013aaa3a6f2
Create Date: 2022-04-19 09:33:21.962434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8366fec7806d'
down_revision = '4013aaa3a6f2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
