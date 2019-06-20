# -*- coding: utf-8 -*-

name = "embree"

version = "3.5.2"

description = "embree"

variants = [
    ['gcc-6.3.1'],
]

requires = [
    "tbb-2017.6"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

