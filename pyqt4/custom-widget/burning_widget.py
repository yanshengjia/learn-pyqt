#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
这是我们在 Nero、K3B 或其他 CD 烧录软件中看到的窗口组件。

本例中，我们有一个 QSlider 和一个自定义窗口组件，滑块用来控制自定义窗口组件。
该窗口组件图形化的显示媒体的总量和可用的空余空间。
自定义的窗口不见的最小值是1，最大值是750。如果到达700，将开始绘制红色。通常表示超刻。
烧录部件通常放在窗体的下部，使用一个 QHBoxLayout 和一个 QVBoxLayout 来达到目的。
"""


import sys
from PyQt4 import QtGui, QtCore

# 烧录窗口组件基于 QWidget 窗口组件
class BurningWidget(QtGui.QWidget):

    def __init__(self):
        super(BurningWidget, self).__init__()

        self.initUI()

    def initUI(self):

        self.setMinimumSize(1, 30)      # 修改窗口组件最小size，默认值对于我们有点小
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

        self.connect(self, QtCore.SIGNAL("updateBurningWidget(int)"),
            self.setValue)


    def setValue(self, value):

        self.value = value


    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()


    def drawWidget(self, qp):
        # 使用比默认值更小的字体，更适合我们的需求
        font = QtGui.QFont('Serif', 7, QtGui.QFont.Light)
        qp.setFont(font)

        # 动态绘制窗口组件，当窗口变大时，烧录窗口组件也跟着变大，反之亦然。这正是为什么我们必须计算部件的尺寸到我们自定义的部件。 
        # till 参数决定绘制的所有尺寸。 
        # value 从滑块获得，这是整个区域的比例。
        # full 参数决定我们开始绘制红色的点。注意使用浮点算术，为了实现更高的精度。
        # 实际的绘制由三步组成。我们绘制黄色或红色和黄色矩形，然后绘制垂直线条，把部件分割多部分，最后绘制数字，用来指示媒体的容量。
        size = self.size()
        w = size.width()
        h = size.height()
        step = int(round(w / 10.0))
        till = int(((w / 750.0) * self.value))
        full = int(((w / 750.0) * 700))

        if self.value >= 700:
            qp.setPen(QtGui.QColor(255, 255, 255))
            qp.setBrush(QtGui.QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QtGui.QColor(255, 175, 175))
            qp.setBrush(QtGui.QColor(255, 175, 175))
            qp.drawRect(full, 0, till-full, h)
        else:
            qp.setPen(QtGui.QColor(255, 255, 255))
            qp.setBrush(QtGui.QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)


        pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1,
            QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(QtCore.Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)

        j = 0

        for i in range(step, 10*step, step):

            qp.drawLine(i, 0, i, 5)

            # 我们使用自体度量来绘制文本，我们必须知道文本的宽度，这样才能在垂直线的中间绘制文本
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i-fw/2, h/2, str(self.num[j]))
            j = j + 1


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.setRange(1, 750)
        slider.setValue(75)
        slider.setGeometry(30, 40, 150, 30)

        self.wid = BurningWidget()

        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'),
            self.changeValue)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Burning')

    # 当我们移动滑块， changeValue() 方法被调用
    # 在该方法中我们发送一个自定义的 updateBurningWidget(int) 信号及相应参数，参数是滑块的当前值
    # 该值稍后用来计算烧录部件的容量并绘制
    def changeValue(self, value):

        self.wid.emit(QtCore.SIGNAL("updateBurningWidget(int)"), value)
        self.wid.repaint()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()