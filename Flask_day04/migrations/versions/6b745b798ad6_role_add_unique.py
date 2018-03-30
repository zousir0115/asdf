"""role_add_unique

Revision ID: 6b745b798ad6
Revises: 687ba518b10b
Create Date: 2018-03-27 12:21:35.868987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b745b798ad6'
down_revision = '687ba518b10b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'roles', ['info'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('info', 'roles', type_='unique')
    # ### end Alembic commands ###