#!/usr/bin/python
# -*- coding: utf-8 -*-

# QFileDialog 允许用户选择文件或文件夹，可选择文件来打开和保存。
# 显示一个菜单，中间放置一个文本编辑框，还有一个状态栏。状态机仅为了设计目的显示。菜单项显示 QFileDialog 来选择文件，文件的内容加载进文本编辑器。

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QtGui.QTextEdit()     # 文本编辑框
        self.setCentralWidget(self.textEdit)  # 文本编辑框置于中间
        self.statusBar()
        self.setFocus()

        openFile = QtGui.QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        self.connect(openFile, QtCore.SIGNAL('triggered()'), self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('OpenFile')

    def showDialog(self):
        # 我们弹出 QFileDialog ， getOpenFileName 方法的第一个字符串是标题，第二个字符串指定对话框的工作目录，文件过滤默认设置 All files(*) 。
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                    '/Users/yanshengjia/Desktop')

        # 选择读取的文件，并把文件内容放入文本编辑框
        fname = open(filename)
        data = fname.read()
        self.textEdit.setText(data)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()
