#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
QComboBox 窗口组件允许用户从列表清单中选择。
这个例子中显示一个 QComboBox 和一个 QLabel 。
组合框有5个选项的列表，他们是Linux发行版的名称。标签显示从组合框选择的内容。
'''

from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.label = QtGui.QLabel("Ubuntu", self)

        # 创建一个 QComboBox 窗口组件并增加5个选项。
        combo = QtGui.QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Red Hat")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.label.move(50, 150)

        # 当一个选项被选择，我们调用 onActivated() 方法。
        self.connect(combo, QtCore.SIGNAL('activated(QString)'),
            self.onActivated)

        self.setGeometry(250, 200, 350, 250)
        self.setWindowTitle('QComboBox')

    # 把选择项设置到标签中，并调整标签的尺寸。
    def onActivated(self, text):

        self.label.setText(text)
        self.label.adjustSize()


def main():

    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
