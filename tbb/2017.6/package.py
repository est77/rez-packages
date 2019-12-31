# -*- coding: utf-8 -*-

name = "tbb"

version = "2017.6"

description = "Intel TBB"

variants = [
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
