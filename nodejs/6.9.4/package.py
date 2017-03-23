# -*- coding: utf-8 -*-

name = "nodejs"

version = "6.9.4"

description = "NodeJS"

tools = [
    "node",
    "npm"
]

def commands():
    env.PATH.append("{root}/bin")
