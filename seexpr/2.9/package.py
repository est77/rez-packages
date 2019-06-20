# -*- coding: utf-8 -*-

name = "seexpr"

version = "2.9"

description = "SeExpr"

variants = [
    ['gcc-4.8.3'],
    ['gcc-6.3.1']
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    #env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
