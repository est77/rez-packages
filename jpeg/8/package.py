# -*- coding: utf-8 -*-

name = "jpeg"

version = "8"

description = "LibJPEG"

variants = [
    ['gcc-4.8.3'],
    ['gcc-6.3.1'], 
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

