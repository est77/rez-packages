# -*- coding: utf-8 -*-

name = "jpeg"

version = "8"

description = "LibJPEG"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

