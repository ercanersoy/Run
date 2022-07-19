#
# main-window.py - Run main window script
#
# Copyright (c) 2021-2022 Ercan Ersoy
#
# Author: Ercan Ersoy
#

###########
# Imports #
###########

import about_dialog

import subprocess

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


#####################
# Main Window Class #
#####################

class MainWindow(object):
    def __init__(self, app):
        self.run_with_terminal_emulator = False
        self.run_with_root_privileges = False

        self.App = app

        self.builder = Gtk.Builder().new_from_file('/usr/share/run/ui/main-window.glade')
        self.builder.connect_signals(self)

        self.MainWindow = self.builder.get_object('main-window')
        self.MainWindow.set_application(self.App)
        self.MainWindow.show()

    def onDestroy(self):
        self.MainWindow.destroy()

    def run_with_terminal_emulator_toggle(self, button):
        run_with_terminal_emulator_checkbox = \
            self.builder.get_object('run-with-terminal-'
                                    'emulator-checkbox')
        self.run_with_terminal_emulator = \
            run_with_terminal_emulator_checkbox.get_active()

    def run_with_root_privileges_toggle(self, button):
        run_with_root_privileges_checkbox = \
            self.builder.get_object('run-with-root-'
                                    'privileges-checkbox')
        self.run_with_root_privileges = \
            run_with_root_privileges_checkbox.get_active()

    def run(self, button):
        command_entry = self.builder.get_object('command-entry')
        command_line = command_entry.get_text().split(' ')

        if len(command_line) != 0:
            if self.run_with_root_privileges:
                command_line.insert(0, 'pkexec')

            if self.run_with_terminal_emulator:
                command_line.insert(0, '-e')
                command_line.insert(0, 'x-terminal-emulator')

            subprocess.call(command_line)

            self.onDestroy()

    def information(self, button):
        dialog = about_dialog.AboutDialog()

    def exit_program(self, button):
        self.onDestroy()
