# !/usr/bin/python
# coding=utf8

# 菜单栏集合了应用程序中所有可用的命令
# 我发现 MacOS 下不管怎么设置菜单栏的第一列，最终显示结果还是系统自带的python程序的菜单栏第一列

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('menubar')

        exit = QtGui.QAction("Quit", self)
        exit.setShortcut('Command+Q')   # 设置动作的快捷键
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        # 创建菜单栏
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        # edit = menubar.addMenu('&Edit')
        # view = menubar.addMenu('&View')


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
