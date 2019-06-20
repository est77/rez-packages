# -*- coding: utf-8 -*-

name = "python"

version = "3.6.5"

description = "Python"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

