"""reactions table

Revision ID: 56b0a8517e42
Revises: 834b1a697901
Create Date: 2018-10-17 21:50:51.945195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56b0a8517e42'
down_revision = '834b1a697901'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reaction_name'), 'reaction', ['name'], unique=False)
    op.create_index(op.f('ix_reaction_timestamp'), 'reaction', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reaction_timestamp'), table_name='reaction')
    op.drop_index(op.f('ix_reaction_name'), table_name='reaction')
    op.drop_table('reaction')
    # ### end Alembic commands ###
