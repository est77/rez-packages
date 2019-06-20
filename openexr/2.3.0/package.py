# -*- coding: utf-8 -*-

name = "openexr"

version = "2.3.0"

description = "openexr"

variants = [
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
