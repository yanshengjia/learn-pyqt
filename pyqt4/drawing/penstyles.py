#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
QPen 是初级图形对象，用来绘制线条、曲线和矩形、椭圆、多边形或其他形状的轮廓。
该本例中，我们绘制了6条线，使用了不同的画笔样式。
其中5个预定义样式，我们也可以创建自定义样式，最后一个使用了自定义的样式。
'''

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('penstyles')

    def paintEvent(self, e):

        qp = QtGui.QPainter()

        qp.begin(self)
        self.doDrawing(qp)
        qp.end()

    def doDrawing(self, qp):
        # 创建一个 QPen 对象，颜色为黑色，宽度为2个像素，以便能够看到各种画笔样式间的不同。
        # QtCore.Qt.SolidLine 是其中一种预定义的画笔样式。
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(QtCore.Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(QtCore.Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(QtCore.Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(QtCore.Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        # 这里我们自定义了一个画笔样式，设置 QtCore.Qt.CustomDashLine 样式，并调用 setDashPattern() 方法。
        # 用一列数字定义样式，数字的数量必须是偶数，奇数定义 dash 或者 numbers space，数字越大，dash 或者 numbers space 越大。
        # 我们的样式是 1px dash, 4px space, 5px dash, 4px space。
        pen.setStyle(QtCore.Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

if __name__ == '__main__':
    main()
