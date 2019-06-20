# -*- coding: utf-8 -*-

name = "gcc"

version = "6.3.1"

description = "gcc"

tools = [
    "gcc",
    "g++",
    "gcc63",
    "g++63"
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.CC.set("{root}/bin/g++")
    env.CXX.set("{root}/bin/gcc")
