# -*- coding: utf-8 -*-

name = "lcms"

version = "2.9"

description = "Little CMS"

variants = [
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
