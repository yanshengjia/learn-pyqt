#!/usr/bin/python
# -*- coding: utf-8 -*-

# 简单的对话框，以便从用户获取单个值。输入值可以是一个字符串，一个数字或者列表的一项。

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 一个按钮，无焦点策略
        self.button = QtGui.QPushButton('Dialog', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button.move(20, 20)
        # 按按钮会调出对话框来获取值，输入的值显示在单行编辑框中
        self.connect(self.button, QtCore.SIGNAL('clicked()'),
            self.showDialog)
        self.setFocus()

        # 一个单行编辑器
        self.label = QtGui.QLineEdit(self)
        self.label.move(130, 22)

        self.setWindowTitle('InputDialog')
        self.setGeometry(300, 300, 350, 80)


    def showDialog(self):
        # 显示输入对话框，第一个字符串是对话框标题，第二个字符串是对话框中消息
        # 对话框返回输入的文本和一个布尔值。点击ok按钮，布尔值为True，否则为False
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter your name:')

        if ok:
            self.label.setText(str(text))


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
