# -*- coding: utf-8 -*-

name = "maya"

version = "2015"

description = "Maya"

requires = [
    "tiff-3"
]

has_plugins = True

tools = [
    "maya",
    "Render"
]

def commands():
    env.MAYA_LOCATION.set("/usr/autodesk/maya2015-x64")
    env.PATH.prepend("/usr/autodesk/maya2015-x64/bin")
