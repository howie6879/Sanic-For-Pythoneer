#!/usr/bin/env python
"""
 Created by howie.hu at 12/01/2018.
"""
import sqlalchemy as sa

metadata = sa.MetaData()

user = sa.Table(
    'user',
    metadata,
    sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
    sa.Column('user_name', sa.String(16), nullable=False),
    sa.Column('pwd', sa.String(32), nullable=False),
    sa.Column('real_name', sa.String(6), nullable=False),
)
