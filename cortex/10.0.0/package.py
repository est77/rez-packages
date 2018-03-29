# -*- coding: utf-8 -*-

name = "cortex"

version = "10.0.0"

description = "Cortex"

requires = [
    "boost-1.61.0",
    "openexr-2.2.0",
    "oiio-1.7",
    "alembic-1.7.1",
    "glew-2.1.0",
    "tbb-4.3",
    "pyimath-2.2.0"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
    env.IECOREGL_SHADER_PATHS.append("{root}/glsl")
    env.IECOREGL_SHADER_INCLUDE_PATHS.append("{root}/glsl")

    if 'appleseed' in resolve:
        env.APPLESEED_SEARCHPATH.append("{root}/appleseedDisplays")
