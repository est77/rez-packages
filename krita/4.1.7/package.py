# -*- coding: utf-8 -*-

name = "krita"

version = "4.1.7"

description = "Krita"

tools = [
    "krita"
]

def commands():
    env.PATH.append("{root}")
