"""Remove first name and last name from users

Revision ID: 104d4aad20e0
Revises: ecbd3b6d72dc
Create Date: 2023-04-19 17:14:47.284160

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '104d4aad20e0'
down_revision = 'ecbd3b6d72dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', mysql.VARCHAR(length=255), nullable=True))
        batch_op.add_column(sa.Column('last_name', mysql.VARCHAR(length=255), nullable=True))

    # ### end Alembic commands ###
