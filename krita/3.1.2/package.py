# -*- coding: utf-8 -*-

name = "krita"

version = "3.1.2"

description = "Krita"

tools = [
    "krita"
]

def commands():
    env.PATH.append("{root}")
