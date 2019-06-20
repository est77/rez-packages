# -*- coding: utf-8 -*-

name = "glu"

version = "9.0.0"

description = "GLU"

variants = [
    ['gcc-4.8.3'],
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
