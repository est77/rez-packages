# -*- coding: utf-8 -*-

name = "blenderseed"

version = "0.7.0"

description = "blenderseed"

requires = [
    "appleseed"
]

def commands():
    env.BLENDER_USER_SCRIPTS.append("{root}")
