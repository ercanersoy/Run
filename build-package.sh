#!/bin/sh
#
# build-package.sh - Run build package script
#
# Copyright (c) 2022 Ercan Ersoy
#
# Author: Ercan Ersoy
#

python3 setup.py --command-packages=stdeb.command bdist_deb
