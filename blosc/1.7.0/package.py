# -*- coding: utf-8 -*-

name = "blosc"

version = "1.7.0"

variants = [
    ['gcc-4.8.3'],
]

description = "blosc"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
