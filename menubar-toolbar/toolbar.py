# !/usr/bin/python
# coding=utf8

# 工具栏提供了快速访问最常用的命令功能
# 感觉此功能比较鸡肋，用菜单栏就够了

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('toolbar')

        self.exit = QtGui.QAction('Quit', self)
        self.exit.setShortcut('Command+Q')
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        # 工具栏
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exit)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
