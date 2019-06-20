# -*- coding: utf-8 -*-

name = "hdf5"

version = "1.8.15"

description = "HDF5"

variants = [
    ['gcc-4.8.3'],
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
