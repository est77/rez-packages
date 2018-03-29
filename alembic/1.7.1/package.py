# -*- coding: utf-8 -*-

name = "alembic"

version = "1.7.1"

description = "Alembic"

requires = [
    "hdf5-1.8.15",
    "openexr-2.2"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
