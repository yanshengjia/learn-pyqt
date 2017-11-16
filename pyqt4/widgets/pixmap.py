#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
QPixmap 是处理图像的窗口组件之一，非常适合在屏幕上显示图像。
在我们的代码示例里，我们使用 QPixmap 在窗口中显示图像。
在下面的例子中，我们在窗口中显示图像。
'''


from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("rotunda.jpg")   # 图片无法加载

        label = QtGui.QLabel(self)
        label.setPixmap(pixmap)

        hbox.addWidget(label)
        self.setLayout(hbox)

        self.setWindowTitle("Rotunda in Skalica")
        self.move(250, 200)


def main():

    app = QtGui.QApplication([])
    exm = Example()
    exm.show()
    app.exec_()


if __name__ == '__main__':
    main()