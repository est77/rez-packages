# -*- coding: utf-8 -*-

name = "cortex"

version = "9.16.2"

description = "Cortex"

requires = [
    "boost-1.55.0",
    "openexr-2.2.0",
    "oiio-1.7"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
    env.IECOREGL_SHADER_PATHS.append("{root}/glsl")
    env.IECOREGL_SHADER_INCLUDE_PATHS.append("{root}/glsl")

    if 'appleseed' in resolve:
        env.APPLESEED_SEARCHPATH.append("{root}/appleseedDisplays")
