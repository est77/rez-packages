# -*- coding: utf-8 -*-

name = "tiff"

version = "4.0.10"

description = "TIFF lib"

variants = [
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
