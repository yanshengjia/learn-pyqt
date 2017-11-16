#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
颜色是指一个代表红（Red）、绿（Green）、蓝（Blue）（RGB）强度值组合的对象，有效的RGB值在0~255之间。
我们可以用多种方式定义颜色，最常用的是RGB十进制或者十六进制值。
也可以使用RGBA值，表示红（Red）、绿（Green）、蓝（Blue）和透明度（Alpha）。这里我们增加了额外的信息——关于透明度。Alpha值是255表明完全不透明，0是全透明，即颜色不可见。
在这个例子中，我们绘制了9个有色矩形，第一行显示红色，具有不同的透明度。
'''

import sys, random
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 350, 280)
        self.setWindowTitle('Colors')

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)

        self.drawRectangles(qp)

        qp.end()

    def drawRectangles(self, qp):

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')  # 使用十六进制符号定义颜色
        qp.setPen(color)

        # 这里我们定义一个画刷并绘制一个矩形，画刷从一个初级图形对象，用来绘制图形的背景。
        # drawRect() 方法接受四个参数。
        # 头两个是坐标轴的x和y，第三和第四个是矩形的宽高，该方法使用当前的画笔和画刷绘制一个矩形。
        qp.setBrush(QtGui.QColor(255, 0, 0, 80))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QtGui.QColor(255, 0, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QtGui.QColor(255, 0, 0, 255))
        qp.drawRect(250, 15, 90, 60)

        qp.setBrush(QtGui.QColor(10, 163, 2, 55))
        qp.drawRect(10, 105, 90, 60)

        qp.setBrush(QtGui.QColor(160, 100, 0, 255))
        qp.drawRect(130, 105, 90, 60)

        qp.setBrush(QtGui.QColor(60, 100, 60, 255))
        qp.drawRect(250, 105, 90, 60)

        qp.setBrush(QtGui.QColor(50, 50, 50, 255))
        qp.drawRect(10, 195, 90, 60)

        qp.setBrush(QtGui.QColor(50, 150, 50, 255))
        qp.drawRect(130, 195, 90, 60)

        qp.setBrush(QtGui.QColor(223, 135, 19, 255))
        qp.drawRect(250, 195, 90, 60)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

if __name__ == '__main__':
    main()