"""add backup_id

Revision ID: 67a444e698ec
Revises: 80bca57bea52
Create Date: 2023-06-02 09:09:24.935046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67a444e698ec'
down_revision = '80bca57bea52'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('backup_records',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('backup_id', sa.UUID(), nullable=True),
    sa.Column('status', sa.Enum('scheduled', 'running', 'finished', 'failed', name='backupstatus'), nullable=True),
    sa.Column('destination', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('backup_records')
    # ### end Alembic commands ###