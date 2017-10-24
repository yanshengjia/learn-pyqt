# !/usr/bin/python
# coding=utf8

# 实现一个小窗体

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 150) # (width, height)
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())
