# -*- coding: utf-8 -*-

name = "alembic"

version = "1.7.11"

description = "Alembic"

variants = [
    ['gcc-6.3.1'],
]

requires = [
    "openexr-2.3"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
