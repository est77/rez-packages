# -*- coding: utf-8 -*-

name = "llvm"

version = "3.4"

description = "LLVM"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
