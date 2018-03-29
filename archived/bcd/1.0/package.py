# -*- coding: utf-8 -*-

name = "bcd"

version = "1.0"

description = "Bayesian collaborative denoiser"

tools = [
    "bcd_cli"
]

def commands():
    env.PATH.append("{root}")
