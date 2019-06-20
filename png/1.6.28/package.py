# -*- coding: utf-8 -*-

name = "png"

version = "1.6.28"

description = "LibPNG"

variants = [
    ['gcc-4.8.3'],
    ['gcc-6.3.1'],
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
