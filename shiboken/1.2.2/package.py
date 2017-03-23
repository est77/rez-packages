# -*- coding: utf-8 -*-

name = "shiboken"

version = "1.2.2"

description = "Shiboken"

requires = [
    "python-2.7"
]

tools = [
    "shiboken"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
