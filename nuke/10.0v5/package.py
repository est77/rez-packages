# -*- coding: utf-8 -*-

name = "Nuke"

version = "10.0v5"

description = "Nuke"

requires = [
    "glu-9.0",
]

tools = [
    "Nuke10.0"
]

def commands():
    env.PATH.append("{root}")
    alias("nuke", "Nuke{this.version.major}.0")
