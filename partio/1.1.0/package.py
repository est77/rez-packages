# -*- coding: utf-8 -*-

name = "partio"

version = "1.1.0"

description = "Partio"

requires = [
    "seexpr-2.9"
]

tools = [
    "partattr",
    "partconv",
    "partinfo",
    "partview"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    #env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
