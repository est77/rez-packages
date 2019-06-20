# -*- coding: utf-8 -*-

name = "embree"

version = "3.2.0"

description = "Embree"

variants = [
    ['gcc-4.8.3'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
