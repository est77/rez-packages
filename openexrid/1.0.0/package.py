# -*- coding: utf-8 -*-

name = "openexrid"

version = "1.0.0"

description = "OpenEXRId"

requires = []

build_requires = []

def commands():
    env.OFX_PLUGIN_PATH.append("{root}/openfx")

