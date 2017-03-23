# -*- coding: utf-8 -*-

name = "pyimath"

version = "2.2.0"

description = "pyimath"

requires = [
    "openexr-2.2.0",
    "boost-1.55.0"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7")
