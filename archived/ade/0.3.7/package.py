# -*- coding: utf-8 -*-

name = "ade"

version = "0.3.7"

description = "A templated file system manager"

requires = ["python-2.7"]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/source")
