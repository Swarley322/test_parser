"""empty message

Revision ID: 619f9b62be49
Revises: 4449c4045f01
Create Date: 2020-04-04 19:32:10.705886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '619f9b62be49'
down_revision = '4449c4045f01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('City', sa.Column('inexpensive_meal_price', sa.Float(), nullable=True))
    op.add_column('City', sa.Column('internet', sa.Float(), nullable=True))
    op.add_column('City', sa.Column('one_way_ticket', sa.Float(), nullable=True))
    op.add_column('City', sa.Column('restaurant_2_persons', sa.Float(), nullable=True))
    op.add_column('City', sa.Column('water_033', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('City', 'water_033')
    op.drop_column('City', 'restaurant_2_persons')
    op.drop_column('City', 'one_way_ticket')
    op.drop_column('City', 'internet')
    op.drop_column('City', 'inexpensive_meal_price')
    # ### end Alembic commands ###
