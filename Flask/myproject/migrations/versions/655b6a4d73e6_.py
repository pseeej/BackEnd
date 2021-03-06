"""empty message

Revision ID: 655b6a4d73e6
Revises: 8acd06c9f1cd
Create Date: 2021-02-19 21:29:26.446172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '655b6a4d73e6'
down_revision = '8acd06c9f1cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
