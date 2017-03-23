# -*- coding: utf-8 -*-

name = "png"

version = "1.6.28"

description = "LibPNG"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
