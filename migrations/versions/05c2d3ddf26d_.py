"""empty message

Revision ID: 05c2d3ddf26d
Revises: a96b4f40c581
Create Date: 2019-12-17 09:07:49.836429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05c2d3ddf26d'
down_revision = 'a96b4f40c581'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_track_alias', table_name='track')
    op.create_index(op.f('ix_track_alias'), 'track', ['alias'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_track_alias'), table_name='track')
    op.create_index('ix_track_alias', 'track', ['alias'], unique=1)
    # ### end Alembic commands ###