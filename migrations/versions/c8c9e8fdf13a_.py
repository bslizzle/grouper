"""empty message

Revision ID: c8c9e8fdf13a
Revises: 02b71316d5a8
Create Date: 2019-04-17 09:34:34.516179

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c8c9e8fdf13a'
down_revision = '02b71316d5a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_request',
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('uin', sa.Integer(), nullable=False),
    sa.Column('requester_fname', sa.String(length=60), nullable=True),
    sa.Column('requester_lname', sa.String(length=60), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.project_id'], ),
    sa.ForeignKeyConstraint(['uin'], ['profile.uin'], ),
    sa.PrimaryKeyConstraint('project_id', 'uin')
    )
    op.drop_table('request')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request',
    sa.Column('project_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('uin', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('requester_fname', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('requester_lname', mysql.VARCHAR(length=60), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.project_id'], name='request_ibfk_1'),
    sa.ForeignKeyConstraint(['uin'], ['profile.uin'], name='request_ibfk_2'),
    sa.PrimaryKeyConstraint('project_id', 'uin'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('project_request')
    # ### end Alembic commands ###
