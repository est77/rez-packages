# -*- coding: utf-8 -*-

name = "sodium"

version = "1.0.4"

description = "Sodium"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
