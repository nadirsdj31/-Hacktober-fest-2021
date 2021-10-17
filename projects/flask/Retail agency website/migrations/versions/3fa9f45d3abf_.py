"""empty message

Revision ID: 3fa9f45d3abf
Revises: 32915b1b9be9
Create Date: 2020-05-14 01:54:04.169681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fa9f45d3abf'
down_revision = '32915b1b9be9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Houses_agent_id_fkey', 'Houses', type_='foreignkey')
    op.drop_column('Houses', 'agent_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Houses', sa.Column('agent_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('Houses_agent_id_fkey', 'Houses', 'Agents', ['agent_id'], ['id'])
    # ### end Alembic commands ###