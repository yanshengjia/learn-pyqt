# !/usr/bin/python
# coding=utf8

# 用编程的方式关闭窗体：退出按钮

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class QuitButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit Button')

        quit = QtGui.QPushButton('Close', self)     # 按钮上文本为Close,父类是self(也就是QWidget窗体)
        quit.setGeometry(10, 10, 64, 35)

        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))   # 信号槽，quit按钮被单击后发出信号『被单击』到槽『退出应用』，槽发出信号『退出』

app = QtGui.QApplication(sys.argv)
qb = QuitButton()
qb.show()
app.exit(app.exec_())
