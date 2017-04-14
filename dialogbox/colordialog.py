#!/usr/bin/python
# -*- coding: utf-8 -*-

# 选择颜色的对话框

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        color = QtGui.QColor(0, 0, 0)   # 黑色

        self.button = QtGui.QPushButton('Dialog', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)

        self.connect(self.button, QtCore.SIGNAL('clicked()'),
            self.showDialog)
        self.setFocus()

        self.widget = QtGui.QWidget(self)
        self.widget.setStyleSheet("QWidget { background-color: %s }"
            % color.name())
        self.widget.setGeometry(130, 22, 100, 100)

        self.setWindowTitle('ColorDialog')
        self.setGeometry(300, 300, 250, 180)


    def showDialog(self):
        # 弹出一个 QColorDialog 颜色对话框
        col = QtGui.QColorDialog.getColor()

        # 检查颜色是否有效，如果点击了取消按钮，将返回无效的颜色。如果颜色有些，我们使用样式修改背景颜色。
        if col.isValid():
            self.widget.setStyleSheet("QWidget { background-color: %s }"
                % col.name())


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
