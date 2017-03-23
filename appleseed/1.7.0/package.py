# -*- coding: utf-8 -*-

name = "appleseed"

version = "1.7.0"

description = "appleseed"

requires = [
    "xercesc-3",
    "boost-1.55.0",
    "openexr-2.2.0",
    "oiio-1.7",
    "osl-1.7",
    "seexpr"
]

tools = [
    "appleseed.cli"
]

def commands():
    env.APPLESEED.set("{root}")
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7")
