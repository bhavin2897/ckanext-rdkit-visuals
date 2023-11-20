"""remoce package_id from molecules table

Revision ID: 49ff7076d8b0
Revises: 1f5e9a1c52dd
Create Date: 2023-11-14 08:53:07.445148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49ff7076d8b0'
down_revision = '1f5e9a1c52dd'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('molecules', 'package_id')


def downgrade():
    pass

