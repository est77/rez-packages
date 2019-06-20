# -*- coding: utf-8 -*-

name = "tbb"

version = "4.3"

description = "Intel TBB"

variants = [
    ['gcc-4.8.3'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
