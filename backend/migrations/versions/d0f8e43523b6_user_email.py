"""user: email

Revision ID: d0f8e43523b6
Revises: 040ea53baaa0
Create Date: 2024-09-07 18:27:45.659678

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d0f8e43523b6"
down_revision: Union[str, None] = "040ea53baaa0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("email", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "email")
    # ### end Alembic commands ###
