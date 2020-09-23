"""empty message

Revision ID: 7380aae3ced7
Revises: 
Create Date: 2020-09-22 15:37:24.621175

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '7380aae3ced7'
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
    op.create_table('threads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('genre_id', sa.String(length=10), nullable=False),
    sa.Column('book_id', sa.String(length=255), nullable=True),
    sa.Column('createTime', sa.DateTime(), nullable=False),
    sa.Column('updateTime', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('threads')
    op.drop_table('genres')
    # ### end Alembic commands ###
