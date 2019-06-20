# -*- coding: utf-8 -*-

name = "qt"

version = "5.12.0"

description = "Qt"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.QT_PLUGIN_PATH.set("{root}/plugins")
