# -*- coding: utf-8 -*-

name = "alshaders"

version = "1.0.0RC19"

description = "alShaders"

def commands():
    if 'maya' in resolve:
        env.ARNOLD_PLUGIN_PATH.append("{root}/bin")
        env.MTOA_TEMPLATES_PATH.append("{root}/ae")
        env.MAYA_CUSTOM_TEMPLATE_PATH.append("{root}/aexml")
