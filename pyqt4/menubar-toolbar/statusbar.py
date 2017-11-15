# !/usr/bin/python
# coding=utf8

# 状态栏，显示状态信息的窗口组件

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('statusbar')

        self.statusBar().showMessage('Ready')   # 状态栏

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
