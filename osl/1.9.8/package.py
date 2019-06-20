# -*- coding: utf-8 -*-

name = "osl"

version = "1.9.8"

description = "OpenShadingLanguage"

variants = [
    ['gcc-4.8.3'],
]

requires = [
    "llvm-5.0.1",
    "openexr-2.2.0",
    "oiio-1.8.9",
    "pugixml-1.9"
]

tools = [
    "oslc",
    "oslinfo"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
