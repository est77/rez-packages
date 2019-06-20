# -*- coding: utf-8 -*-

name = "blenderseed"

version = "1.0.0"

description = "blenderseed"

variants = [
    ['blender-2.79'],
    ['blender-2.80'],
]

requires = [
    "tbb-2017"
]

def commands():
    if "blender" in resolve:
        if resolve.blender.version.minor == 80:
            env.APPLESEED.set("/hdd/Devel/appleseedhq/appleseed/sandbox")
            env.PYTHONPATH.append("$APPLESEED/lib/Ship/python")
        elif resolve.blender.version.minor == 79:
            env.APPLESEED.set("/hdd/Devel/appleseedhq/appleseed4/sandbox")
        else:
   	        error("Unsupported blender version")

    env.BLENDER_USER_SCRIPTS.append("{root}")
    env.LD_LIBRARY_PATH.append("$APPLESEED/lib/Ship")
    env.APPLESEED_BIN_DIR.set("$APPLESEED/bin/Ship")
    env.APPLESEED_PYTHON_PATH.set("$APPLESEED/lib/Ship/python")
