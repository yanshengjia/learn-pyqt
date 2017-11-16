#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
我们从在窗口客户区绘制一些Unicode文本开始。
在下面的例子中，我们绘制一些西里尔字母的文本，文正水平和垂直居中对齐。
'''

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Draw Text')

        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
                    \u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
                    \u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

    # 在绘制事件中绘画
    def paintEvent(self, event):
        # QPainter 类负责所有的低级绘画。
        # 所有的绘制方法都在 begin() 和 end() 方法之间。
        # 这里实际的绘制是代理给了 drawText() 方法。
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()


    def drawText(self, event, qp):
        # 这里我们定义了画笔和字体，用来绘制文本
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)     # drawText() 方法在窗口上绘制文本， 绘制事件的 rect() 方法返回需要更新的矩形

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

if __name__ == '__main__':
    main()
