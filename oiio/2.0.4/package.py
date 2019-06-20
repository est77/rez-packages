# -*- coding: utf-8 -*-

name = "oiio"

version = "2.0.4"

description = "OpenImageIO"

variants = [
    ['gcc-6.3.1'],
]

requires = [
    "boost-1.61.0",
    "openexr-2.3.0",
    "tiff-4.0.10",
    "png-1.6",
    "jpeg-8",
    "ocio-1.1.0"
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
