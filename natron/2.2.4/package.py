# -*- coding: utf-8 -*-

name = "Natron"

version = "2.2.4"

description = "Natron"

tools = [
    "Natron",
    "NatronRenderer"
]

def commands():
    env.PATH.append("{root}/bin")
