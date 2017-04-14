# !/usr/bin/python
# coding=utf8

# 用 sender() 方法知道是哪个组件发出的信号

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        button1 = QtGui.QPushButton("Button 1", self)
        button1.move(30, 50)

        button2 = QtGui.QPushButton("Button 2", self)
        button2.move(150, 50)


        # 2个按钮都连接了同一个信号
        self.connect(button1, QtCore.SIGNAL('clicked()'),
            self.buttonClicked)

        self.connect(button2, QtCore.SIGNAL('clicked()'),
            self.buttonClicked)

        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Event sender')
        self.resize(290, 150)


    def buttonClicked(self):

        sender = self.sender()
        # 通过调用 sender() 方法我们确定信号来源。在程序的状态栏，我们显示按下的按钮的标签。
        self.statusBar().showMessage(sender.text() + ' was pressed')

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
