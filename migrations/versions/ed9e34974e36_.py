"""empty message

Revision ID: ed9e34974e36
Revises: e970af6f46ea
Create Date: 2017-04-05 17:06:22.563515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed9e34974e36'
down_revision = 'e970af6f46ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('fullname', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('nickname', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'nickname')
    op.drop_column('user', 'fullname')
    # ### end Alembic commands ###