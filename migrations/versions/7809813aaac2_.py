"""empty message

Revision ID: 7809813aaac2
Revises: cdea3ed2b6fc
Create Date: 2017-03-02 15:05:09.478695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7809813aaac2'
down_revision = 'cdea3ed2b6fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('desc', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'desc')
    # ### end Alembic commands ###