# -*- coding: utf-8 -*-

name = "resolve"

version = "12.5.5"

description = "Resolve"

tools = [
    "resolve"
]

def commands():
    env.PATH.append("/opt/resolve/bin")
