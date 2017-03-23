# -*- coding: utf-8 -*-

name = "tiff"

version = "3.8.2"

description = "TIFF lib"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
