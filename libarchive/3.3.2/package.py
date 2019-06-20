# -*- coding: utf-8 -*-

name = "libarchive"

version = "3.3.2"

description = "LibArchive"

variants = [
    ['gcc-4.8.3'],
]

tools = [
    "bsdcat",
    "bsdcpio",
    "bsdtar"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
