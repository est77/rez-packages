# -*- coding: utf-8 -*-

name = "tuttle"

version = "0.13.3"

description = "tuttle"

tools = [
    "sam",
    "sam-cp",
    "sam-do",
    "sam-ls",
    "sam-mv",
    "sam-rm"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
    env.OFX_PLUGIN_PATH.append("{root}/OFX")
