# -*- coding: utf-8 -*-

name = "Fusion"

version = "8.2"

description = "Blackmagic Fusion"

tools = [
    "Fusion"
]

def commands():
    env.PATH.append("{root}")
