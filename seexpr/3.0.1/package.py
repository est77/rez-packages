# -*- coding: utf-8 -*-

name = "seexpr"

version = "3.0.1"

description = "SeExpr"

variants = [
    ['gcc-6.3.1']
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
