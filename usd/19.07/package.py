# -*- coding: utf-8 -*-

name = "usd"

version = "19.07"

description = "USD"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python")


