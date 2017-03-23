# -*- coding: utf-8 -*-

name = "seexpr"

version = "2.9"

description = "SeExpr"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    #env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
