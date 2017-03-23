# -*- coding: utf-8 -*-

name = "ffmpeg"

version = "3.2.2"

description = "ffmpeg"

tools = [
    "ffmpeg"
]

def commands():
    env.PATH.append("{root}")
