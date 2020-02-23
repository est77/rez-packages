# -*- coding: utf-8 -*-

name = "osl"

version = "1.10.9"

description = "OSL"

variants = [
    ['gcc-6.3.1'],
]

requires = [
    "oiio-2.1.11",
    "llvm-8.0.0"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

