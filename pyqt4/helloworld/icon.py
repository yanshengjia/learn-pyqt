# !/usr/bin/python
# coding=utf8

# 在标题栏左上角显示应用程序图标
# 在 MacOS 和 Ubuntu 中，图标并不会显示在标题栏上，本程序适用于 Windows

import sys
from PyQt4 import QtGui


class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('icons/web.png'))


app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())
