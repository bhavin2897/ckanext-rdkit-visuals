"""add new molecule relation data table

Revision ID: 1f5e9a1c52dd
Revises: 2e23c588066e
Create Date: 2023-11-13 13:57:44.835974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f5e9a1c52dd'
down_revision = '2e23c588066e'
branch_labels = None
depends_on = None

'''molecule relation data table with molecules and package'''

def upgrade():
    op.create_table('molecule_rel_data',
                    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
                    sa.Column('package_id', sa.UnicodeText(), sa.ForeignKey('package.id'), nullable=False),
                    sa.Column('molecules_id',sa.Integer, sa.ForeignKey('molecules.id'), nullable=False),
                    )


def downgrade():
    pass
