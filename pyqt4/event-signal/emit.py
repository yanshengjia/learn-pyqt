# !/usr/bin/python
# coding=utf8

# 从 QtCore.QObject 继承的对象可以发射信号。如果点击按钮，将产生一个 clicked() 信号。
# 在接下来的例子中可以看到如何发射信号。

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # connect(sender, signal, slot)
        # 把手工创建的 closeEmitApp() 信号和 close() 槽连接。
        self.connect(self, QtCore.SIGNAL('closeEmitApp()'),
            QtCore.SLOT('close()'))

        self.setWindowTitle('emit')
        self.resize(250, 150)


    def mousePressEvent(self, event):
        # 创建一个名为 closeEmitApp() 的新信号，在鼠标的按下实践中发射该信号。
        self.emit(QtCore.SIGNAL('closeEmitApp()'))


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
