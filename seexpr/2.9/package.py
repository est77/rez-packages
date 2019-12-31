# -*- coding: utf-8 -*-

name = "seexpr"

version = "2.9"

description = "SeExpr"

variants = [
    ['gcc-6.3.1']
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
