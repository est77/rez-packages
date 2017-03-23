# -*- coding: utf-8 -*-

name = "zmq"

version = "4.2.1"

description = "ZMQ"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
