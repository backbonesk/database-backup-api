"""add created_at

Revision ID: 80bca57bea52
Revises: 3813c5fa96ef
Create Date: 2023-06-01 15:25:23.131065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80bca57bea52'
down_revision = '3813c5fa96ef'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('backup_records',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('status', sa.Enum('scheduled', 'running', 'finished', 'failed', name='backupstatus'), nullable=True),
    sa.Column('destination', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('backups',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('host', sa.String(), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('dbname', sa.String(), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('rrule', sa.String(), nullable=True),
    sa.Column('destination', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('scheduled', 'running', 'finished', 'failed', name='backupstatus'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'created_at')
    op.drop_table('backups')
    op.drop_table('backup_records')
    # ### end Alembic commands ###