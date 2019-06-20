# -*- coding: utf-8 -*-

name = "materiax"

version = "1.36.3"

description = "MaterialX"

variants = [
    ['gcc-6.3.1'],
]

requires = [
    "oiio-2.0.4"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/python")

