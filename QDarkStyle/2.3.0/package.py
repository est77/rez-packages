# -*- coding: utf-8 -*-

name = u'QDarkStyle'

version = '2.3.0'

description = \
    """
    A dark stylesheet for PyQt/PySide applications
    """

variants = [['platform-linux', 'arch-x86_64', 'os-CentOS-7.3.1611', 'python-2.7']]

def commands():
    env.PYTHONPATH.append('{root}/python')

timestamp = 1487170685
