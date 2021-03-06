"""json test

Revision ID: ec88e206f366
Revises: 
Create Date: 2020-04-16 19:43:57.078448

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ec88e206f366'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('airport_id',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('airport_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('airport_id'),
    sa.UniqueConstraint('city')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('eng_part_of_the_world', sa.String(), nullable=True),
    sa.Column('ru_part_of_the_world', sa.String(), nullable=True),
    sa.Column('eng_name', sa.String(), nullable=True),
    sa.Column('ru_name', sa.String(), nullable=True),
    sa.Column('eng_country', sa.String(), nullable=True),
    sa.Column('ru_country', sa.String(), nullable=True),
    sa.Column('city_img', sa.String(), nullable=True),
    sa.Column('inexpensive_meal_price', sa.Float(), nullable=True),
    sa.Column('restaurant_2_persons', sa.Integer(), nullable=True),
    sa.Column('water_033', sa.Integer(), nullable=True),
    sa.Column('one_way_ticket', sa.Integer(), nullable=True),
    sa.Column('internet', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('eng_name'),
    sa.UniqueConstraint('ru_name')
    )
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('json_test', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('role', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_role'), 'user', ['role'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('attraction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('img_url', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_attraction_city_id'), 'attraction', ['city_id'], unique=False)
    op.create_table('avg_price_reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('avg_reviews', sa.Integer(), nullable=True),
    sa.Column('avg_week_price', sa.Integer(), nullable=True),
    sa.Column('avg_day_price', sa.Integer(), nullable=True),
    sa.Column('parsing_date', sa.String(), nullable=True),
    sa.Column('week_number', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_avg_price_reviews_city_id'), 'avg_price_reviews', ['city_id'], unique=False)
    op.create_table('hotel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('week_price', sa.Integer(), nullable=True),
    sa.Column('avg_day_price', sa.Integer(), nullable=True),
    sa.Column('checkin_date', sa.String(), nullable=True),
    sa.Column('checkout_date', sa.String(), nullable=True),
    sa.Column('hotel_link', sa.String(), nullable=True),
    sa.Column('parsing_date', sa.String(), nullable=True),
    sa.Column('week_number', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('reviews', sa.Integer(), nullable=True),
    sa.Column('stars', sa.String(), nullable=True),
    sa.Column('distance_from_center', sa.String(), nullable=True),
    sa.Column('img_url', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hotel_city_id'), 'hotel', ['city_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_hotel_city_id'), table_name='hotel')
    op.drop_table('hotel')
    op.drop_index(op.f('ix_avg_price_reviews_city_id'), table_name='avg_price_reviews')
    op.drop_table('avg_price_reviews')
    op.drop_index(op.f('ix_attraction_city_id'), table_name='attraction')
    op.drop_table('attraction')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_role'), table_name='user')
    op.drop_table('user')
    op.drop_table('test')
    op.drop_table('city')
    op.drop_table('airport_id')
    # ### end Alembic commands ###
