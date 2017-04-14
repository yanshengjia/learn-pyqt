# !/usr/bin/python
# coding=utf8

# 组件在网格中跨越多列或多行

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()   # 单行编辑框
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()  # 文本编辑框

        # 网格布局
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)     # 各个控件的上下间距，setMargin()是控件与窗体之间的左右边距

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)  # 在(3, 1)处放置文本编辑框，跨越5行1列

        self.setLayout(grid)

        self.setWindowTitle('grid layout')
        self.resize(350, 300)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
