# -*- coding: utf-8 -*-

name = "openvdb"

version = "4.0.2"

description = "OpenVDB"

variants = [
    ['gcc-4.8.3'],
]

requires = [
    "boost-1.61.0",
    "openexr-2.2.0",
    "blosc-1.7.0",
    "tbb-2017.6"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7")
