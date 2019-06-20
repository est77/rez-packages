# -*- coding: utf-8 -*-

name = "openexr"

version = "2.2.0"

description = "openexr"

variants = [
    ['gcc-4.8.3'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
