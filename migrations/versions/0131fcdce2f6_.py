"""empty message

Revision ID: 0131fcdce2f6
Revises: 
Create Date: 2018-09-04 12:17:36.288250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0131fcdce2f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('location', sa.String(length=128), nullable=True),
    sa.Column('desc', sa.String(length=2048), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_date'), 'event', ['date'], unique=False)
    op.create_index(op.f('ix_event_desc'), 'event', ['desc'], unique=False)
    op.create_index(op.f('ix_event_location'), 'event', ['location'], unique=False)
    op.create_index(op.f('ix_event_title'), 'event', ['title'], unique=False)
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('team', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('photo_url', sa.String(length=120), nullable=True),
    sa.Column('role', sa.String(length=120), nullable=True),
    sa.Column('is_executive', sa.Boolean(), nullable=True),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_member_email'), 'member', ['email'], unique=False)
    op.create_index(op.f('ix_member_is_executive'), 'member', ['is_executive'], unique=False)
    op.create_index(op.f('ix_member_name'), 'member', ['name'], unique=False)
    op.create_index(op.f('ix_member_role'), 'member', ['role'], unique=False)
    op.create_index(op.f('ix_member_team'), 'member', ['team'], unique=False)
    op.create_index(op.f('ix_member_username'), 'member', ['username'], unique=False)
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('tags', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=16384), nullable=True),
    sa.Column('is_veep_x', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_description'), 'project', ['description'], unique=False)
    op.create_index(op.f('ix_project_tags'), 'project', ['tags'], unique=False)
    op.create_index(op.f('ix_project_title'), 'project', ['title'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_project_title'), table_name='project')
    op.drop_index(op.f('ix_project_tags'), table_name='project')
    op.drop_index(op.f('ix_project_description'), table_name='project')
    op.drop_table('project')
    op.drop_index(op.f('ix_member_username'), table_name='member')
    op.drop_index(op.f('ix_member_team'), table_name='member')
    op.drop_index(op.f('ix_member_role'), table_name='member')
    op.drop_index(op.f('ix_member_name'), table_name='member')
    op.drop_index(op.f('ix_member_is_executive'), table_name='member')
    op.drop_index(op.f('ix_member_email'), table_name='member')
    op.drop_table('member')
    op.drop_index(op.f('ix_event_title'), table_name='event')
    op.drop_index(op.f('ix_event_location'), table_name='event')
    op.drop_index(op.f('ix_event_desc'), table_name='event')
    op.drop_index(op.f('ix_event_date'), table_name='event')
    op.drop_table('event')
    # ### end Alembic commands ###