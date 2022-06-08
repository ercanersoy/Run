#!/usr/bin/env python3

#
# setup.py - Setup file for Run
#
# Copyright (c) 2021-2022 Ercan Ersoy
#
# Author: Ercan Ersoy
#

###########
# Imports #
###########

from run.version import version
from setuptools import setup, find_packages

import os

#####################
# Translation Files #
#####################

ui_files = []
for ui_file in os.listdir('ui'):
    ui_files.append('ui/' + ui_file)

os.system('msgfmt --check '
          '--output-file=locale/en/LC_MESSAGES/run.mo '
          'locale/en/LC_MESSAGES/run.po')

os.system('msgfmt --check '
          '--output-file=locale/tr/LC_MESSAGES/run.mo '
          'locale/tr/LC_MESSAGES/run.po')

data_files = [
    ('/usr/share/applications', ['data/net.ercanersoy.run.desktop']),
    ('/usr/share/locale/en/LC_MESSAGES',
        ['locale/en/LC_MESSAGES/run.mo']),
    ('/usr/share/locale/tr/LC_MESSAGES',
        ['locale/tr/LC_MESSAGES/run.mo']),
    ('/usr/share/run/ui', ui_files)
]

#########
# Setup #
#########

setup(
    name='Run',
    version=version,
    packages=find_packages(),
    scripts=['bin/run'],
    install_requires=['PyGObject'],
    data_files=data_files,
    author='Ercan Ersoy',
    author_email='ercanersoy@ercanersoy.net',
    description='A helper application for running program',
    license='GPLv2+',
    keywords='run execute',
    url='https://ercanersoy.net',
)
