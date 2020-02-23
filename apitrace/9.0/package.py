# -*- coding: utf-8 -*-

name = "apitrace"

version = "9.0"

description = "apitrace"

requires = [
    "qt-5",
]

def commands():
    env.PATH.append("{root}/bin")
    #env.LD_LIBRARY_PATH.append("{root}/lib")

