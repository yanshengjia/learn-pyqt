# !/usr/bin/python
# coding=utf8

# 将菜单栏、工具栏和状态栏放在一起

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(640, 480)
        self.setWindowTitle('mainwindow')
        self.center()

        # 编辑框
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        # 动作 Action
        exit = QtGui.QAction('Quit', self)
        exit.setShortcut('Command+Q')
        # exit.setStatusTip('Quit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        # 状态栏
        self.statusBar().showMessage('Hello')

        # 菜单栏
        menubar = self.menuBar()
        file = menubar.addMenu('&Menu')
        file.addAction(exit)
        edit = menubar.addMenu('&Edit')
        view = menubar.addMenu('&View')

        # 工具栏
        toolbar = self.addToolBar('Quit')
        toolbar.addAction(exit)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()    # 计算屏幕像素，获取屏幕宽高
        size = self.geometry()  # 获取窗体宽高
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)   # 将窗体移到屏幕中心，向右向下移动


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
