# -*- coding: utf-8 -*-

name = "baldavenger"

version = "1.0.0"

description = "Baldavenger OFX"

requires = [
    "cuda"
]

build_requires = []

def commands():
    env.OFX_PLUGIN_PATH.append("{root}/openfx")

