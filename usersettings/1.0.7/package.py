# -*- coding: utf-8 -*-

name = u'usersettings'

version = '1.0.7'

description = "usersettings"

variants = [['platform-linux', 'arch-x86_64', 'os-CentOS-7.3.1611', 'python-2.7']]

def commands():
    env.PYTHONPATH.append('{root}/python')


