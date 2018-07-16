"""new fields in user model

Revision ID: 739b215febe2
Revises: b0c4ecf0c3b9
Create Date: 2018-07-10 20:26:29.437136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '739b215febe2'
down_revision = 'b0c4ecf0c3b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
