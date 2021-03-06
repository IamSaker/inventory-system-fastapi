"""Pre order column

Revision ID: bc0cb4a96bcd
Revises: 4a184fadff38
Create Date: 2021-09-10 07:42:15.510324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc0cb4a96bcd'
down_revision = '4a184fadff38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('is_preorder', sa.Boolean(), nullable=False))
    op.add_column('orders', sa.Column('preorder_date', sa.Date(), nullable=True))
    op.create_index(op.f('ix_orders_preorder_date'), 'orders', ['preorder_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_preorder_date'), table_name='orders')
    op.drop_column('orders', 'preorder_date')
    op.drop_column('orders', 'is_preorder')
    # ### end Alembic commands ###
