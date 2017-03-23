# -*- coding: utf-8 -*-

name = "glu"

version = "9.0.0"

description = "GLU"

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
