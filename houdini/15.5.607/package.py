# -*- coding: utf-8 -*-

name = "houdini"

version = "15.5.607"

description = "Houdini 15"

tools = [
    "houdini"
]

def commands():
    env.HFS.set("/opt/hfs15.5.607")
    env.H.set("${HFS}")
    env.HB.set("${H}/bin")
    env.HDSO.set("${H}/dsolib")
    env.HD.set("${H}/demo")
    env.HH.set("${H}/houdini")
    env.HHC.set("${HH}/config")
    env.HT.set("${H}/toolkit")
    env.HSB.set("${HH}/sbin")

    env.TEMP.set("/tmp")
    env.LD_LIBRARY_PATH.prepend("${HDSO}")
    env.PATH.prepend("${HB}:${HSB}")

    env.HOUDINI_MAJOR_RELEASE.set("15")
    env.HOUDINI_MINOR_RELEASE.set("5")
    env.HOUDINI_BUILD_VERSION.set("607")
    env.HOUDINI_VERSION.set("${HOUDINI_MAJOR_RELEASE}.${HOUDINI_MINOR_RELEASE}.${HOUDINI_BUILD_VERSION}")

    env.HOUDINI_BUILD_KERNEL.set("2.6.32-431.20.5.el6.x86_64")
    env.HOUDINI_BUILD_PLATFORM.set("Red Hat Enterprise Linux Workstation release 6.5 (Santiago)")
    env.HOUDINI_BUILD_COMPILER.set("4.8.2")
    env.HOUDINI_BUILD_LIBC.set("glibc 2.12")

    env.HIH.set("${HOME}/houdini${HOUDINI_MAJOR_RELEASE}.${HOUDINI_MINOR_RELEASE}")
    env.HIS.set("$HH")
