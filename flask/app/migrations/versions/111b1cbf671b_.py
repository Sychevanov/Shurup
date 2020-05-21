"""empty message

Revision ID: 111b1cbf671b
Revises: 
Create Date: 2020-04-05 19:40:39.565668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '111b1cbf671b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    # ### end Alembic commands ###
