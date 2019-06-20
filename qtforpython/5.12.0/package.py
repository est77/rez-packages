# -*- coding: utf-8 -*-

name = "qtforpython"

version = "5.12.0"

description = "QtForPython"

variants = [
    ['python-3.6'],
]

requires = [
    "qt-5.12.0"
]

tools = [
    "pyside-lupdate",
    "pyside-rcc",
    "pyside-uic"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python")
