# -*- coding: utf-8 -*-

name = "Nuke"

version = "11.1v1"

description = "Nuke"

requires = [
    "glu"
]

tools = [
    "Nuke11.1"
]

def commands():
    env.PATH.append("/usr/local/Nuke11.1v1")
    alias("nuke", "Nuke{this.version.major}.1 -nc")
