"""empty message

Revision ID: 7408c872d6c0
Revises: 4d81578a84d3
Create Date: 2019-05-15 15:31:00.388640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7408c872d6c0"
down_revision = "4d81578a84d3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "participant_hacknight",
        sa.Column("participant_id", sa.Integer(), nullable=True),
        sa.Column("hacknight_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["hacknight_id"], ["hacknight.id"]),
        sa.ForeignKeyConstraint(["participant_id"], ["participant.id"]),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("participant_hacknight")
    # ### end Alembic commands ###
