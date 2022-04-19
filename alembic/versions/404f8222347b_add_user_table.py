"""add user table

Revision ID: 404f8222347b
Revises: bb534734ba76
Create Date: 2022-04-19 09:22:26.603163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '404f8222347b'
down_revision = 'bb534734ba76'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
