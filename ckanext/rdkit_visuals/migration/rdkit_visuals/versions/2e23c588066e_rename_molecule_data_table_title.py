"""rename molecule data table title

Revision ID: 2e23c588066e
Revises: 51fd43f24eaf
Create Date: 2023-11-13 13:52:41.790144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e23c588066e'
down_revision =   '51fd43f24eaf' #This is temporary, will be removed soon.
branch_labels = None
depends_on = None

'''renamed molecule_data table title to molecules'''
def upgrade():
    op.rename_table('molecule_data', 'molecules')


def downgrade():
    pass
