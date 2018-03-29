# -*- coding: utf-8 -*-

name = "gaffer"

version = "0.45.0.0"

description = "Gaffer"

requires = [
    "python-2.7",
    "subprocess32",
    "PyOpenGL",
    "tbb-4.3",
    "cortex",
    "osl-1.8.10",
    "alembic-1.7.1",
    "qt-4.8",
    "pyside-1.2",
    "ocio-1.0.9",
    "openvdb-4.0.2"
]

tools = [
    "gaffer"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.GAFFERUI_QT_BINDINGS.set("PySide")
    env.GAFFERUI_FONT_SIZE.set("12")
