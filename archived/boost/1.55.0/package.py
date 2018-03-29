# -*- coding: utf-8 -*-

name = "boost"

version = "1.55.0"

description = "boost"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
