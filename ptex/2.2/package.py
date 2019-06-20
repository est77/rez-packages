# -*- coding: utf-8 -*-

name = "ptex"

version = "2.2"

description = "Ptex"

variants = [
    ['gcc-4.8.3'],
]

tools = [
    "ptxinfo"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
