"""empty message

Revision ID: ccc82b102b64
Revises: 1a3bba9950dd
Create Date: 2019-03-03 15:33:48.777852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccc82b102b64'
down_revision = '1a3bba9950dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties__shown',
    sa.Column('Property_ID', sa.Integer(), nullable=False),
    sa.Column('List_Price', sa.Integer(), nullable=True),
    sa.Column('Location', sa.String(length=128), nullable=True),
    sa.Column('Trend_Link', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('Property_ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties__shown')
    # ### end Alembic commands ###
