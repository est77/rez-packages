# -*- coding: utf-8 -*-

name = "tbb"

version = "4.3"

description = "Intel TBB"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
