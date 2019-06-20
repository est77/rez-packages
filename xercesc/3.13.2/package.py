# -*- coding: utf-8 -*-

name = "xercesc"

version = "3.13.2"

description = "Xerces-C"

variants = [
    ['gcc-6.3.1'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

