# -*- coding: utf-8 -*-

name = "scons"

version = "3.1.2"

description = "SCons"

def commands():
    env.PATH.append("{root}/bin")
