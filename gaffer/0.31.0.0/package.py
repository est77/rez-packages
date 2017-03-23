# -*- coding: utf-8 -*-

name = "gaffer"

version = "0.31.0.0"

description = "Gaffer"

requires = [
    "cortex",
    "osl",
    "alembic-1.6",
    "appleseed"
]

tools = [
    "gaffer"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    #env.PYTHONPATH.prepend("{root}/lib/python2.7")
    #env.PYTHONPATH.prepend("{root}/lib/python2.7/lib-dynload")
