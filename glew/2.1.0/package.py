# -*- coding: utf-8 -*-

name = "glew"

version = "2.1.0"

description = "GLEW"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
