# -*- coding: utf-8 -*-

name = "appleseed"

version = "1.9.0"

description = "appleseed"

requires = [
    "xercesc-3",
    "boost-1.61.0",
    "openexr-2.2.0",
    "oiio-1.7.15",
    "osl-1.8.10",
    "seexpr",
    "ocio-1.0.9"
]

tools = [
    "appleseed.cli"
]

def commands():
    env.APPLESEED.set("{root}")
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7")

    if 'gaffer' in resolve:
        env.OSL_SHADER_PATHS.append("{root}/shaders/appleseed")
        env.APPLESEED_SEARCHPATH.append("{root}/shaders/appleseed")
