# -*- coding: utf-8 -*-

name = "appleseed"

version = "2.1.0"

description = "appleseed"

variants = [
    ['gcc-6.3.1'],
]

requires = [
    "boost-1.61",
    "xercesc-3",
    "openexr-2.3.0",
    "osl-1.10.3",
    "seexpr",
    "embree-3.5.2"
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
