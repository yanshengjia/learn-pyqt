# !/usr/bin/python
# coding=utf8

# 绝对定位
# 写死程序的界面是很不好的

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QtGui.QLabel('Zetcode', self)
        label1.move(15, 10) # 向右移动15个像素，像下移动10像素，初始位置在窗体左上角

        label2 = QtGui.QLabel('tutorials for programmers', self)
        label2.move(35, 40)

        self.setWindowTitle('Absolute')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
