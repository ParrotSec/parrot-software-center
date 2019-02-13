#!/usr/bin/env python3

# -*- coding: utf-8 -*-
#
#  untitled.py
#
#  Copyright 2019 Lorenzo "Palinuro" Faletra <palinuro@parrotsec.org>,
#                 Claudio La Barbera <vattelappesca@boh.tld>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import sys, os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebKitWidgets import QWebView


class PWebView(QWebView):
    def __init__(self):
        self.view = QWebView.__init__(self)
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)

    def adjustTitle(self):
        self.setWindowTitle(self.title())


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    web = PWebView()
    window.setCentralWidget(web)
    window.show()
    window.resize(900, 600)
    window.setWindowTitle("Parrot Software Center")
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/index.html"))
    web.load(QUrl(QUrl.fromLocalFile(file_path)))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
