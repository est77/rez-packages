# -*- coding: utf-8 -*-

name = "openvdb"

version = "4.0.2"

description = "OpenVDB"

requires = [
    "boost-1.61.0",
    "openexr-2.2.0",
    "blosc-1.7.0",
    "tbb-4.3"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7")
