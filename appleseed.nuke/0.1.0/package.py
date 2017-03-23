# -*- coding: utf-8 -*-

name = "appleseed.nuke"

version = "0.1.0"

description = "appleseed-nuke"

requires = [
    "appleseed"
]

def commands():
    if 'nuke' in resolve:
        env.NUKE_PATH.append("{root}/plugins")
        env.NUKE_PATH.append("{root}/menu")
        env.PYTHONPATH.append("{root}/scripts")
