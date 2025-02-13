"""empty message

Revision ID: 9fcf6e01f0e7
Revises: a009e280be35
Create Date: 2021-05-10 19:41:16.393774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fcf6e01f0e7'
down_revision = 'a009e280be35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('task_goal_task_id_fkey', 'task', type_='foreignkey')
    op.drop_column('task', 'goal_task_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_task_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('task_goal_task_id_fkey', 'task', 'goal', ['goal_task_id'], ['goal_id'])
    # ### end Alembic commands ###
