# -*- coding: utf-8 -*-

name = "boost"

version = "1.61.0"

description = "boost"

variants = [
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
