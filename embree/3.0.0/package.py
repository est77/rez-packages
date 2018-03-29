# -*- coding: utf-8 -*-

name = "embree"

version = "3.0.0"

description = "Embree"

requires = [
    "tbb-4.3"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
