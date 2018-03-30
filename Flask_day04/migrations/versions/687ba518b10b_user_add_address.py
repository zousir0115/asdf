"""user_add_address

Revision ID: 687ba518b10b
Revises: e13a5191bc38
Create Date: 2018-03-27 12:18:59.857934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '687ba518b10b'
down_revision = 'e13a5191bc38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('address', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'address')
    # ### end Alembic commands ###