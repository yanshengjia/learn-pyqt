# !/usr/bin/python
# coding=utf8

# 屏幕中央显示窗体

import sys
from PyQt4 import QtGui

class Center(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('center')
        self.resize(640, 480)
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()    # 计算屏幕像素，获取屏幕宽高
        size = self.geometry()  # 获取窗体宽高
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)   # 将窗体移到屏幕中心，向右向下移动


app = QtGui.QApplication(sys.argv)
qb = Center()
qb.show()
app.exit(app.exec_())
