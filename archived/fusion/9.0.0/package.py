# -*- coding: utf-8 -*-

name = "Fusion"

version = "9.0.0"

description = "Blackmagic Fusion"

tools = [
    "Fusion"
]

def commands():
    env.PATH.append("/opt/BlackmagicDesign/Fusion9")
