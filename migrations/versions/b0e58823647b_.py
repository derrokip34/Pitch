"""empty message

Revision ID: b0e58823647b
Revises: 
Create Date: 2020-05-05 13:04:38.296618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0e58823647b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('dislikes', sa.Integer(), nullable=True))
    op.add_column('posts', sa.Column('likes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'likes')
    op.drop_column('posts', 'dislikes')
    # ### end Alembic commands ###