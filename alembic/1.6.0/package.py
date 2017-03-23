# -*- coding: utf-8 -*-

name = "alembic"

version = "1.6.0"

description = "Alembic"

requires = [
    "boost-1.55.0",
    "openexr-2.2.0",
    "hdf5-1.8.15"
]

tools = [
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    #env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
