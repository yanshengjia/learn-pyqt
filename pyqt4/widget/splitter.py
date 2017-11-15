#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
QSplitter 使得用户可以通过拖动子窗口组件的边界来控制子窗口组件的尺寸。
在我们的例子中，我们显示由两个分离器组织的三个 QFrame 窗口组件。
例子中有三个框架窗口组件和两个分离器。
'''

from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        hbox = QtGui.QHBoxLayout(self)

        # 为了看到 QFrame 之间的边界，我们使用带样式的框架。
        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.Box)

        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.Box)

        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.Box)

        # 创建一个 QSplitter 并加入两个框架。
        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        # 也可以把一个分离器加到另一个分离器窗口组件中。
        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setWindowTitle('QSplitter')
        # 使用 Cleanlooks 样式。 在某些样式中，框架是不可见的。
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        self.setGeometry(250, 200, 350, 250)


def main():

    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
