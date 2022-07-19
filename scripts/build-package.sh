#!/bin/sh
#
# build-package.sh - Package builder of Run
#
# Copyright (c) 2022 Ercan Ersoy
#
# Author: Ercan Ersoy
#

dpkg-deb --build ../run
