# -*- coding: utf-8 -*-

name = "rsync"

version = "3.1.2"

description = "rsync"

tools = [
    "rsync"
]

def commands():
    env.PATH.append("{root}")
