# !/usr/bin/python
# coding=utf8

# 网格布局
# 最常用的布局类是网格布局，网格布局把空间划分为行和列。

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('grid layout')

        # 20个元素的字符串数组
        names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/',
            '4', '5', '6', '*', '1', '2', '3', '-',
            '0', '.', '=', '+']

        # 网格布局
        grid = QtGui.QGridLayout()

        j = 0
        pos = [ (0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3),
                (4, 0), (4, 1), (4, 2), (4, 3)]

        for i in names:
            button = QtGui.QPushButton(i)
            if j == 2:  # 第一行第三列为空
                grid.addWidget(QtGui.QLabel(''), 0, 2)
            else: grid.addWidget(button, pos[j][0], pos[j][1])  # 给网格中添加按钮
            j = j + 1

        # 设置网格布局
        self.setLayout(grid)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
