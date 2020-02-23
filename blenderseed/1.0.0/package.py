# -*- coding: utf-8 -*-

name = "blenderseed"

version = "1.0.0"

description = "blenderseed"

requires = [
    "tbb-2017"
]

def commands():
    env.APPLESEED.set("/hdd/Devel/appleseedhq/appleseed/sandbox")
    env.PYTHONPATH.append("$APPLESEED/lib/Ship/python")
    env.BLENDER_USER_SCRIPTS.append("{root}")
    env.LD_LIBRARY_PATH.append("$APPLESEED/lib/Ship")
    env.APPLESEED_BIN_DIR.set("$APPLESEED/bin/Ship")
    env.APPLESEED_PYTHON_PATH.set("$APPLESEED/lib/Ship/python")

