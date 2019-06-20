# -*- coding: utf-8 -*-

name = "osl"

version = "1.10.3"

description = "OSL"

variants = [
    ['gcc-6.3.1'],
]

requires = [
    "oiio-2.0.4",
    "llvm-5.0.1"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

