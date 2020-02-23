# -*- coding: utf-8 -*-

name = "blender"

version = "2.82"

description = "Blender"

tools = [
  "blender"
]

def commands():
    env.PATH.append("{root}")
    alias("blenderx", "blender --python-use-system-env")

