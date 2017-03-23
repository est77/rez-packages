# -*- coding: utf-8 -*-

name = "oiio"

version = "1.7.10"

description = "OpenImageIO"

requires = [
    "boost-1.55.0",
    "freetype-2.7",
    "openexr-2.2.0",
    "tiff-3.8",
    "png-1.6"
]

build_requires = [
    "cmake",
    "boost-1.55.0",
    "freetype-2.7",
    "openexr-2.2.0",
    "tiff-3.8",
    "png-1.6"
]

tools = [
    "iconvert",
    "idiff",
    "igrep",
    "iinfo",
    "iv",
    "maketx",
    "oiiotool"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    #env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
