# -*- coding: utf-8 -*-

name = "pyside"

version = "1.2.2"

description = "PySide"

requires = [
    "python-2.7",
    "shiboken-1.2.2",
    "qt-4.8"
]

tools = [
    "pyside-lupdate",
    "pyside-rcc",
    "pyside-uic"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
