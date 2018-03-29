# -*- coding: utf-8 -*-

name = "ocio"

version = "1.0.9"

description = "OpenColorIO"

tools = [
    "ociobakelut",
    "ociocheck"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
