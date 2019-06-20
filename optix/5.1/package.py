# -*- coding: utf-8 -*-

name = "optix"

version = "5.1"

description = "NVidia Optix"

requires = [
    "cuda-9.0"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
