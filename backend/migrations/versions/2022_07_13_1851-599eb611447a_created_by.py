"""created_by

Revision ID: 599eb611447a
Revises: af76ec3bad4b
Create Date: 2022-07-13 18:51:06.937002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '599eb611447a'
down_revision = 'af76ec3bad4b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('created_by_id', sa.Integer(), server_default=sa.text('1'), nullable=False))
    op.create_foreign_key('created_by_fkey', 'image', '_user', ['created_by_id'], ['id'])
    op.add_column('landmark', sa.Column('created_by_id', sa.Integer(), server_default=sa.text('1'), nullable=False))
    op.create_foreign_key('created_by_fkey', 'landmark', '_user', ['created_by_id'], ['id'])
    op.add_column('point_cloud', sa.Column('created_by_id', sa.Integer(), server_default=sa.text('1'), nullable=False))
    op.create_foreign_key('created_by_fkey', 'point_cloud', '_user', ['created_by_id'], ['id'])
    op.add_column('room', sa.Column('created_by_id', sa.Integer(), server_default=sa.text('1'), nullable=False))
    op.create_foreign_key('created_by_fkey', 'room', '_user', ['created_by_id'], ['id'])

    op.alter_column('image', 'created_by_id',
                    existing_type=sa.INTEGER(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('landmark', 'created_by_id',
                    existing_type=sa.INTEGER(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('point_cloud', 'created_by_id',
                    existing_type=sa.INTEGER(),
                    server_default=None,
                    existing_nullable=False)
    op.alter_column('room', 'created_by_id',
                    existing_type=sa.INTEGER(),
                    server_default=None,
                    existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('created_by_fkey', 'room', type_='foreignkey')
    op.drop_column('room', 'created_by_id')
    op.drop_constraint('created_by_fkey', 'point_cloud', type_='foreignkey')
    op.drop_column('point_cloud', 'created_by_id')
    op.drop_constraint('created_by_fkey', 'landmark', type_='foreignkey')
    op.drop_column('landmark', 'created_by_id')
    op.drop_constraint('created_by_fkey', 'image', type_='foreignkey')
    op.drop_column('image', 'created_by_id')
    # ### end Alembic commands ###
