# -*- coding: utf-8 -*-

name = u'subprocess32'

version = '3.2.7'

description = \
    """
    A backport of the subprocess module from Python 3.2/3.3 for use on 2.x.
    """

variants = [['platform-linux', 'arch-x86_64', 'os-Fedora-24', 'python-2.7']]

def commands():
    env.PYTHONPATH.append('{root}/python')

timestamp = 1487523402
