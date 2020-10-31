"""empty message

Revision ID: a50e2ed1baf0
Revises: 019f0a5696b3
Create Date: 2020-10-30 21:58:35.094599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a50e2ed1baf0'
down_revision = '019f0a5696b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('stock_quantity', sa.Integer(), nullable=True),
    sa.Column('category', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=64), nullable=True),
    sa.Column('author_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('email', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    op.drop_table('books')
    # ### end Alembic commands ###
