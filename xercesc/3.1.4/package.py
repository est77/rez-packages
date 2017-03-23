# -*- coding: utf-8 -*-

name = "xercesc"

version = "3.1.4"

description = "Xerces-C"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
