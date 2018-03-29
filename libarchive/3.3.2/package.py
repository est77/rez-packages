# -*- coding: utf-8 -*-

name = "libarchive"

version = "3.3.2"

description = "LibArchive"

requires = [
]

build_requires = [
]

tools = [
    "bsdcat",
    "bsdcpio",
    "bsdtar"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
