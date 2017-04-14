#!/usr/bin/python
# -*- coding: utf-8 -*-

# 选择字体的对话框

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 水平框布局
        hbox = QtGui.QHBoxLayout()

        # 一个按钮
        button = QtGui.QPushButton('Dialog', self)
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20, 20)

        hbox.addWidget(button)

        self.connect(button, QtCore.SIGNAL('clicked()'), self.showDialog)

        # 一个标签
        self.label = QtGui.QLabel('Knowledge only matters', self)
        self.label.move(130, 20)

        hbox.addWidget(self.label, 1)   # 伸缩量为1
        self.setLayout(hbox)

        self.setWindowTitle('FontDialog')
        self.setGeometry(300, 300, 250, 110)


    def showDialog(self):
        # 字体选择对话框
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
