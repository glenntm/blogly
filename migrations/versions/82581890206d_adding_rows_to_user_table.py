"""Adding rows to user table

Revision ID: 82581890206d
Revises: 
Create Date: 2024-01-17 20:43:47.779946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82581890206d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',

    )
    # ### end Alembic commands ###
