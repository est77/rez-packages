# -*- coding: utf-8 -*-

name = "gimp"

version = "2.9.7"

description = "gimp"

tools = [
    "gimp"
]

def commands():
    env.PATH.append("{root}/bin")
