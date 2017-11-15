# !/usr/bin/python
# coding=utf8

# 框布局
# 使用布局类管理布局更灵活、更实用
# 这是在窗体上摆放组件的首选方式
# 基本的布局类是 QHBoxLayout 和 QVBoxLayout，它们可以横向和纵向排列窗口组件。

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 创建2个按钮
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        # 水平框布局
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(okButton)
        hbox.addStretch(1)  # 伸缩量为1，可以把伸缩量想象成一个弹簧
        hbox.addWidget(cancelButton)
        # qt 会把没有widget的空白部分根据伸缩量总数等分

        # 将水平局部放到垂直布局中
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 设置窗体的主布局
        self.setLayout(vbox)

        self.setWindowTitle('box layout')
        self.resize(300, 150)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
