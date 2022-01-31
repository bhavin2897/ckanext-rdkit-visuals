"""Add molecular table

Revision ID: e224157c4480
Revises: 
Create Date: 2022-01-31 09:58:35.735287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e224157c4480'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('molecule_data',
                    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
                    sa.Column('package_id', sa.UnicodeText(), sa.ForeignKey('package.id'), nullable=False),
                    sa.Column(u'inchi', sa.UnicodeText()),
                    sa.Column(u'smiles', sa.UnicodeText()),
                    sa.Column(u'inchi_key', sa.UnicodeText()),
                    sa.Column(u'exact_mass', sa.Float())
                    )



def downgrade():
    op.drop_table('molecule_data')
