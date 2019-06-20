# -*- coding: utf-8 -*-

name = "ocio"

version = "1.1.0"

description = "OpenColorIO"

variants = [
    ['gcc-6.3.1'],
]

tools = [
    "ociobakelut",
    "ociocheck"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
