"""empty message

Revision ID: 946c4a58abc4
Revises: 
Create Date: 2020-09-21 13:18:04.280855

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '946c4a58abc4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('createTime', sa.DateTime(), nullable=False),
    sa.Column('updateTime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genres')
    # ### end Alembic commands ###