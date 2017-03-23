# -*- coding: utf-8 -*-

name = "gcc"

version = "4.8.3"

description = "gcc"

tools = [
    "gcc",
    "g++",
    "gcc48",
    "g++48"
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.CC.set("{root}/bin/g++")
    env.CXX.set("{root}/bin/gcc")
