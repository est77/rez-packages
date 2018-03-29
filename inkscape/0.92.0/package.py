# -*- coding: utf-8 -*-

name = "inkscape"

version = "0.9.0"

description = "inkscape"

tools = [
    "inkscape"
]

def commands():
    env.PATH.append("{root}/bin")
