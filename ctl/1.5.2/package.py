# -*- coding: utf-8 -*-

name = "ctl"

version = "1.5.2"

description = "Ampas CTL"

requires = [
    "acescontainer",
    "openexr-2.2.0"
]

tools = [
    "ctlrender",
    "exr_ctl_exr",
    "exrdpx"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
