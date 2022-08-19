"""create_first_table

Revision ID: 325f83331103
Revises: 
Create Date: 2022-08-19 09:41:51.066135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '325f83331103'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cool_plugin_table',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('random_number', sa.Integer, nullable=False),
        sa.Column('name', sa.UnicodeText()),
        sa.Column('dataset', sa.UnicodeText(), sa.ForeignKey('package.name'), nullable=False),        
        sa.Column('created_at', sa.DateTime(timezone=False), nullable=False)
    )


def downgrade():
    op.drop_table('cool_plugin_table')
