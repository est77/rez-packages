# -*- coding: utf-8 -*-

name = "cmake"

version = "3.15.4"

description = "cmake"

tools = [
    "cmake",
    "ccmake",
    "cmake-gui"
]

def commands():
    env.PATH.append("{root}/bin")

