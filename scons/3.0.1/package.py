# -*- coding: utf-8 -*-

name = "scons"

version = "3.0.1"

description = "SCons"

def commands():
    env.PATH.append("{root}/bin")
