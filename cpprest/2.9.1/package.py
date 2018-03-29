# -*- coding: utf-8 -*-

name = "cpprest"

version = "2.9.1"

description = "cpp rest SDK"

requires = [
    "boost-1.61"
]

tools = [
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
