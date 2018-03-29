# -*- coding: utf-8 -*-

name = "blender"

version = "2.78"

description = "Blender"

tools = [
  "blender"
]

def commands():
    env.PATH.append("{root}")

    # For now, just unset PYTHONPATH to avoid Python 2 / 3 incompats.
    env.PYTHONPATH.unset()
