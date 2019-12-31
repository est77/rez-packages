# -*- coding: utf-8 -*-

name = "krita"

version = "4.2.6"

description = "Krita"

tools = [
    "krita"
]

def commands():
    env.PATH.append("{root}/bin/")
