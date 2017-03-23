# -*- coding: utf-8 -*-

name = "gcc"

version = "4.1.2"

description = "gcc"

tools = [
    "gcc",
    "g++",
    "gcc41",
    "g++41"
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.CC.set("{root}/bin/g++")
    env.CXX.set("{root}/bin/gcc")
