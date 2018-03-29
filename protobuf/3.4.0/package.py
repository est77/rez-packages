# -*- coding: utf-8 -*-

name = "protobuf"

version = "3.4.0"

description = "Protocol Buffers"

tools = [
    "protoc"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
