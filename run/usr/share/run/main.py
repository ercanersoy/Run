#!/usr/bin/env python3

#
# run - Run main script
#
# Copyright (c) 2021-2023 Ercan Ersoy
#
# Author: Ercan Ersoy
#

###########
# Imports #
###########

import main_window

import locale
import os
import sys

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gio', '2.0')
from gi.repository import Gtk, Gio


#####################
# Application Class #
#####################

class Run(Gtk.Application):
    def __init__(self, application_id, flags):
        super().__init__(application_id=application_id, flags=flags)
        self.connect("activate", self.open_main_window)

    def open_main_window(self, app):
        self.window = main_window.MainWindow(self)


#################
# Main Function #
#################

def main():
    locale.setlocale(locale.LC_ALL, "")
    locale.bindtextdomain('run', '/usr/share/locale')

    app = Run("net.ercanersoy.run", Gio.ApplicationFlags.FLAGS_NONE)
    return app.run()


if __name__ == '__main__':
    sys.exit(main())
