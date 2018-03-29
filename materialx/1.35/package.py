# -*- coding: utf-8 -*-

name = "materialx"

version = "1.35"

description = "MaterialX"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
