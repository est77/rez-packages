# -*- coding: utf-8 -*-

name = "pugixml"

version = "1.9"

description = "pugixml"

variants = [
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
