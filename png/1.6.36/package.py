# -*- coding: utf-8 -*-

name = "png"

version = "1.6.36"

description = "PNG lib"

variants = [
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

