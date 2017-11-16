#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
在下面的例子中，我们将演示如何拖放一个按钮窗口组件。
该例子中，在窗口上有一个 QPushButton ，如果我们用鼠标左键按下按钮，在控制台打印“press”。
用右键按下并移动按钮，对按钮执行拖放操作。
"""

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

# 创建一个 Button 类，从 QPushButton 继承。
# 重新实现 QPushButton 的两个方法： mouseMoveEvent() 和 mousePressEvent() 
class Button(QtGui.QPushButton):

    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

    # 拖放操作开始的地方
    # 现在已经失效
    def mouseMoveEvent(self, e):

        # 只能使用鼠标右键执行拖放操作，鼠标左键保留给点击操作
        if e.buttons() != QtCore.Qt.RightButton:
            return

        mimeData = QtCore.QMimeData()

        drag = QtGui.QDrag(self)    # 创建一个 QDrag 对象
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.start(QtCore.Qt.MoveAction)   # 拖动对象的 starts() 方法开始拖动操作

    # 如果按下鼠标左键，在控制台打印“press”。注意我们同样调用了父类的 mousePressEvent() 方法，否则我们将看不到按钮被按下。
    def mousePressEvent(self, e):

        QtGui.QPushButton.mousePressEvent(self, e)
        if e.button() == QtCore.Qt.LeftButton:
            print 'press'


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):

        e.accept()

    def dropEvent(self, e):
        # 在 dropEvent() 方法中编写在释放鼠标并且结束拖入操作后将发生什么。找出当前鼠标点的位置并把按钮移到相应位置。
        position = e.pos()
        self.button.move(position)

        # 指定拖入动作的类型，这里是移动动作。
        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()