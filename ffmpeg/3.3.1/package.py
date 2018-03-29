# -*- coding: utf-8 -*-

name = "ffmpeg"

version = "3.3.1"

description = "ffmpeg"

tools = [
    "ffmpeg"
]

def commands():
    env.PATH.append("{root}")
