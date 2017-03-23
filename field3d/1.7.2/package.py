# -*- coding: utf-8 -*-

name = "field3d"

version = "1.7.2"

description = "Field3D"

requires = [
    "boost-1.55.0",
    "openexr-2.2.0"
]

tools = [
    "f3dinfo",
    "f3dmakemip",
    "f3dmerge",
    "f3dsample"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    #env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
