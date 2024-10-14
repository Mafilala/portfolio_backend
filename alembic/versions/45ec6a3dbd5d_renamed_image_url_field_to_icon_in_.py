"""renamed image_url field to icon in skills table

Revision ID: 45ec6a3dbd5d
Revises: 9e4af5643677
Create Date: 2024-10-12 16:59:44.639256

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45ec6a3dbd5d'
down_revision: Union[str, None] = '9e4af5643677'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('skills', sa.Column('icon', sa.String(), nullable=False))
    op.drop_column('skills', 'image_url')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('skills', sa.Column('image_url', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('skills', 'icon')
    # ### end Alembic commands ###
