# -*- coding: utf-8 -*-

name = "freetype"

version = "2.7.1"

description = "Freetype"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
