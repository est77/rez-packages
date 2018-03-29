# -*- coding: utf-8 -*-

name = "nnabla"

version = "0.9.4"

description = "NNabla"

requires = [
    "protobuf-3.4.0",
    "libarchive-3.3.2",
    "hdf5-1.8.15"
]

tools = [
    "nbla"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
