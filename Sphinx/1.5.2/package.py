# -*- coding: utf-8 -*-

name = u'Sphinx'

version = '1.5.2'

description = "Sphinx"

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')

