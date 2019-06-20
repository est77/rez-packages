# -*- coding: utf-8 -*-

name = "zlib"

version = "1.2.11"

description = "ZLib"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

