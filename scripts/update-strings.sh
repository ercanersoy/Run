#!/bin/sh
#
# PROJECT: Python GTK+ Hello World
# DESC: Python GTK+ Hello Update Strings Shell Script
# AUTHOR: Erdem Ersoy
# LICENSE: CC0-1.0
#
# Some changes applied by Ercan Ersoy.

APP_NAME=run
APP_VERSION=0.3

xgettext --default-domain=${APP_NAME} \
         --lang=Glade \
         --from-code=utf-8 \
         --output=../run/usr/share/locale/${APP_NAME}.pot \
         --package-name=${APP_NAME} \
         --package-version=${APP_VERSION} \
         ../run/usr/share/run/ui/main-window.glade

xgettext --default-domain=${APP_NAME} \
         --lang=Glade \
         --join-existing \
         --from-code=utf-8 \
         --output=../run/usr/share/locale/${APP_NAME}.pot \
         --package-name=${APP_NAME} \
         --package-version=${APP_VERSION} \
         ../run/usr/share/run/ui/about-dialog.glade

msgmerge --lang=en \
         --update \
         ../run/usr/share/locale/en/LC_MESSAGES/${APP_NAME}.po \
         ../run/usr/share/locale/${APP_NAME}.pot

msgmerge --lang=tr \
         --update \
         ../run/usr/share/locale/tr/LC_MESSAGES/${APP_NAME}.po \
         ../run/usr/share/locale/${APP_NAME}.pot

msgfmt --check --directory=../run/usr/share/locale/en/LC_MESSAGES/ \
       --output-file=../run/usr/share/locale/en/LC_MESSAGES/${APP_NAME}.mo \
       ${APP_NAME}.po \

msgfmt --check --directory=../run/usr/share/locale/tr/LC_MESSAGES/ \
       --output-file=../run/usr/share/locale/tr/LC_MESSAGES/${APP_NAME}.mo \
       ${APP_NAME}.po \
