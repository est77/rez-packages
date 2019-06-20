# -*- coding: utf-8 -*-

name = "jpegturbo"

version = "2.0.1"

variants = [
    ['gcc-6.3.1'],
]

description = "JPEG Turbo"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

