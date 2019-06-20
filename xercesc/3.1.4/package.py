# -*- coding: utf-8 -*-

name = "xercesc"

version = "3.1.4"

description = "Xerces-C"

variants = [
    ['gcc-4.8.3'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
