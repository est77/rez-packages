# -*- coding: utf-8 -*-

name = "ispc"

version = "1.12"

description = "ISPC"

tools = [
    "ispc"
]

def commands():
    env.PATH.append("{root}/bin")
