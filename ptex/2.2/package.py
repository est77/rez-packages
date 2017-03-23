# -*- coding: utf-8 -*-

name = "ptex"

version = "2.2"

description = "Ptex"

requires = [
]

tools = [
    "ptxinfo"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
