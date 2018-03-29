# -*- coding: utf-8 -*-

name = "osl"

version = "1.8.10"

description = "OpenShadingLanguage"

requires = [
    "llvm-3.4",
    "openexr-2.2.0",
    "oiio-1.7.15"
]

build_requires = [
    "llvm-3.4",
    "openexr-2.2.0",
    "oiio-1.7.15"
]

tools = [
    "oslc",
    "oslinfo"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
