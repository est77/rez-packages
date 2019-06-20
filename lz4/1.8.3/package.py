# -*- coding: utf-8 -*-

name = "lz4"

version = "1.8.3"

description = "LZ4"

variants = [
    ['gcc-4.8.3'],
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
