# -*- coding: utf-8 -*-

name = "OpenSubdiv"

version = "3.3.3"

description = "OpenSubdiv"

variants = [
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
