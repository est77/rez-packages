# -*- coding: utf-8 -*-

name = "clangmetatool"

version = "0.10.0"

description = "clangmetatool"

requires = [
    "llvm-8.0.0"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
