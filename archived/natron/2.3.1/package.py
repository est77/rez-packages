# -*- coding: utf-8 -*-

name = "Natron"

version = "2.3.1"

description = "Natron"

tools = [
    "Natron",
    "NatronRenderer"
]

def commands():
    env.PATH.append("{root}/bin")
