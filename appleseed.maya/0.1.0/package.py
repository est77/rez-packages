# -*- coding: utf-8 -*-

name = "appleseed.maya"

version = "0.1.0"

description = "appleseed-maya"

requires = [
    "appleseed"
]

def commands():
    if 'maya' in resolve:
        env.MAYA_PLUG_IN_PATH.append("{root}/plug-ins/" + str(resolve.maya.version))
        env.MAYA_SCRIPT_PATH.append("{root}/scripts")
        env.PYTHONPATH.append("{root}/scripts")
        env.XBMLANGPATH.append("{root}/icons")
        env.APPLESEED_SEARCHPATH.append("$APPLESEED/shaders/maya")
        env.MAYA_RENDER_DESC_PATH.append("{root}/resources")
        env.MAYA_PRESET_PATH.append("{root}/presets")

        # Disable signal handlers while developing.
        env.MAYA_DEBUG_NO_SIGNAL_HANDLERS.set("1")

    if 'alshaders' in resolve:
        env.APPLESEED_SEARCHPATH.append("$APPLESEED/shaders/alshaders")
