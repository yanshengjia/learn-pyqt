#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
滑块是由一个简单的滑柄的窗口组件。
该滑柄可以前后拖动，通过这种方式我们可以为特定任务选择值。
有时候使用滑块比简单提供数值或使用微调框(spin box)更自然。 QLabel 显示文字或图像。

在下面的例子中我们将显示一个滑块和一个标签。这次，标签将显示一个图像，滑块用来控制标签。
'''

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'),
            self.changeValue)

        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('mute.png'))     # 图片路径有误，无法调出图片
        self.label.setGeometry(160, 40, 80, 30)

        self.setWindowTitle('Slider')
        self.setGeometry(300, 300, 250, 150)


    def changeValue(self, value):
        
        if value == 0:
            self.label.setPixmap(QtGui.QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QtGui.QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QtGui.QPixmap('med.png'))
        else:
            self.label.setPixmap(QtGui.QPixmap('max.png'))


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
