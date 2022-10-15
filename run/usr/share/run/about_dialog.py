#
# about-dialog.py - Run about dialog script
#
# Copyright (c) 2021-2022 Ercan Ersoy
#
# Author: Ercan Ersoy
#

###########
# Imports #
###########

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


#####################
# Main Window Class #
#####################

class AboutDialog(Gtk.AboutDialog):
    def __init__(self):
        self.builder = Gtk.Builder().new_from_file('/usr/share/run/ui/'
                                                   'about-dialog.glade')

        self.AboutDialog = self.builder.get_object('about-dialog')
        self.AboutDialog.run()
        self.AboutDialog.hide()
