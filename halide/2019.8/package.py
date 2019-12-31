# -*- coding: utf-8 -*-

name = "halide"

version = "2019.8"

description = "Halide"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/bin")

