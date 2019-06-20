# -*- coding: utf-8 -*-

name = "oiio"

version = "1.8.9"

description = "OpenImageIO"

variants = [
    ['gcc-4.8.3'],
]

requires = [
    "boost-1.61.0",
    "openexr-2.2.0",
    "tiff-3.8",
    "png-1.6",
    "ocio-1.0.9"
]

build_requires = [
    "cmake",
    "boost-1.61.0",
    "openexr-2.2.0",
    "tiff-3.8",
    "png-1.6",
    "ocio-1.0.9"
]

tools = [
    "iconvert",
    "idiff",
    "igrep",
    "iinfo",
    "maketx",
    "oiiotool"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
