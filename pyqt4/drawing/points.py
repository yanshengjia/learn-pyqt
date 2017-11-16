#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
点是可以绘制的最简单的图形对象，是窗口上的很小的一个区域。
在这个例子中，我们在客户区随机地绘制1000个红点。
'''

import sys, random
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Points')

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):

        qp.setPen(QtCore.Qt.red)    # 使用预定义的颜色常量，把画笔设为红色
        size = self.size()          # 每次我们缩放窗口，都将产生绘制事件。通过 size() 方法得到窗口的尺寸，使用窗口尺寸来把点分布到窗口的客户区。

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)      # 使用 drawPoint() 方法绘制点

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

if __name__ == '__main__':
    main()