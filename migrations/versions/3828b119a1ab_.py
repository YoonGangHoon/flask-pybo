"""empty message

Revision ID: 3828b119a1ab
Revises: d61c500dfd14
Create Date: 2024-07-16 13:54:35.389556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3828b119a1ab'
down_revision = 'd61c500dfd14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
