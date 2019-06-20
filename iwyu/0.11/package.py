# -*- coding: utf-8 -*-

name = "iwyu"

version = "0.11"

description = "include-what-you-use"

tools = [
    "include-what-you-use"
]

def commands():
    env.PATH.append("{root}/bin")
