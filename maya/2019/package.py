# -*- coding: utf-8 -*-

name = "maya"

version = "2019"

description = "Maya"

variants = [
    ['gcc-6.3.1'],
]

has_plugins = True

tools = [
    "maya",
    "Render"
]

def commands():
    env.MAYA_LOCATION.set("/usr/autodesk/maya2019")
    env.PATH.append("/usr/autodesk/maya2019/bin")
