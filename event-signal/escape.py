# !/usr/bin/python
# coding=utf8

# PyQt4中的事件经常被重新实现。
# 在接下来的例子中，重新实现了 keyPressEvent() 处理。

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.setWindowTitle('Escape')
        self.resize(250, 150)

    # 重写了 keyPressEvent()，按下ESC键，程序退出
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
