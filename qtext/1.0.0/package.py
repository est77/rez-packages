# -*- coding: utf-8 -*-

name = "qtext"

version = "1.0.0"

description = "QtExt"

requires = [
    "qtpy"
]

def commands():
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
