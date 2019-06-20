# -*- coding: utf-8 -*-

name = "tiff"

version = "3.8.2"

description = "TIFF lib"

variants = [
    ['gcc-4.8.3'],
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
