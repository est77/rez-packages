# -*- coding: utf-8 -*-

name = "llvm"

version = "8.0.0"

description = "LLVM"

variants = [
    ['gcc-6.3.1'],
]

def commands():
    env.PATH.append("{root}/bin")

