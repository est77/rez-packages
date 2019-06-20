# -*- coding: utf-8 -*-

name = "arnold"

version = "5.3.1.0"

description = "Arnold"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")


