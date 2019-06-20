# -*- coding: utf-8 -*-

name = "maya"

version = "2017"

description = "Maya"

variants = [
    ['gcc-4.8.3'],
]

requires = [
    "tiff-3"
]

has_plugins = True

tools = [
    "maya",
    "Render"
]

def commands():
    env.MAYA_LOCATION.set("/usr/autodesk/maya2017")
    env.PATH.append("/usr/autodesk/maya2017/bin")
