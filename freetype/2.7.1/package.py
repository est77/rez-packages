# -*- coding: utf-8 -*-

name = "freetype"

version = "2.7.1"

description = "Freetype"

variants = [
    ['gcc-4.8.3'],
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
