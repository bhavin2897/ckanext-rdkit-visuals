"""add molecular formula 

Revision ID: 51fd43f24eaf
Revises: e224157c4480
Create Date: 2022-02-10 21:04:31.244806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51fd43f24eaf'
down_revision = 'e224157c4480'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('molecule_data', sa.Column('mol_formula', sa.UnicodeText, nullable=True))


def downgrade():
    pass
