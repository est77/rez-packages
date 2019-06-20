# -*- coding: utf-8 -*-

name = "cuda"

version = "9.0.176"

description = "NVidia CUDA"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
