"""Event_Stream_Video

Revision ID: c2632bfd3db1
Revises: 599eb611447a
Create Date: 2022-07-19 16:32:16.970420

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c2632bfd3db1'
down_revision = '599eb611447a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'event',
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('file_path', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
        sa.Column('pc_id', sa.Integer(), nullable=False),
        sa.Column('is_live', sa.Boolean(), nullable=False),
        sa.Column('created_by_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['created_by_id'], ['_user.id'], name='created_by_fkey'),
        sa.ForeignKeyConstraint(['pc_id'], ['point_cloud.id'], name='event_point_cloud_id_fkey', ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_id'), 'event', ['id'], unique=False)
    op.create_table(
        'stream',
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('image_id', sa.Integer(), nullable=False),
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('created_by_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['created_by_id'], ['_user.id'], name='created_by_fkey'),
        sa.ForeignKeyConstraint(['image_id'], ['image.id'], name='stream_image_id_fkey', ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stream_id'), 'stream', ['id'], unique=False)
    op.create_table(
        'video',
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('image_id', sa.Integer(), nullable=False),
        sa.Column('file_name', sa.String(), nullable=False),
        sa.Column('start_frame', sa.Integer(), nullable=True),
        sa.Column('created_by_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['created_by_id'], ['_user.id'], name='created_by_fkey'),
        sa.ForeignKeyConstraint(['image_id'], ['image.id'], name='stream_image_id_fkey', ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_video_id'), 'video', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_video_id'), table_name='video')
    op.drop_table('video')
    op.drop_index(op.f('ix_stream_id'), table_name='stream')
    op.drop_table('stream')
    op.drop_index(op.f('ix_event_id'), table_name='event')
    op.drop_table('event')
    # ### end Alembic commands ###