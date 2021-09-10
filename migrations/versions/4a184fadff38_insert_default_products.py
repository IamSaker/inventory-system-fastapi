"""insert default products

Revision ID: 4a184fadff38
Revises: f24f44f22000
Create Date: 2021-09-09 07:33:57.696016

"""
from alembic import op
from sqlalchemy import Integer, String
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = '4a184fadff38'
down_revision = 'f24f44f22000'
branch_labels = None
depends_on = None


def upgrade():
    products_table = table('products',
        column('id', Integer),
        column('name', String),
        column('current_inventory', Integer),
        column('default_inventory', Integer),
    )
    op.bulk_insert(products_table,
        [
            {
                'id':1,
                'name':'Dripper',
                'current_inventory':5,
                'default_inventory':10
            },
            {
                'id':2,
                'name':'Chemex',
                'current_inventory':4,
                'default_inventory':8
            },
            {
                'id':3,
                'name':'Siphon',
                'current_inventory':3,
                'default_inventory':7
            },
            {
                'id':4,
                'name':'AeroPress',
                'current_inventory':2,
                'default_inventory':4
            },
            {
                'id':5,
                'name':'Cezve',
                'current_inventory':7,
                'default_inventory':13
            },
        ],
        multiinsert=False
    )


def downgrade():
    pass
