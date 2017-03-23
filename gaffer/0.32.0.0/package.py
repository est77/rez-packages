# -*- coding: utf-8 -*-

name = "gaffer"

version = "0.32.0.0"

description = "Gaffer"

requires = [
    "python-2.7",
    "subprocess32",
    "tbb-4.2",
    "cortex",
    "osl-1.7",
    "alembic-1.6",
    "appleseed-1.7",
    "qt-4.8",
    "pyside-1.2",
    "ocio-1.0.9"
]

tools = [
    "gaffer"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.GAFFERUI_QT_BINDINGS.set("PySide")
