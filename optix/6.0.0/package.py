# -*- coding: utf-8 -*-

name = "optix"

version = "6.0.0"

description = "NVidia Optix"

requires = [
    "cuda-10.1"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
