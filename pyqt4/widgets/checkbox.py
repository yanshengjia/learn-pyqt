#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
QCheckBox （复选框） 是一个由两种状态的窗口组件。 On 和 Off 。
他是一个带标签的框。每段一个复选框被选中和或者清除时，都将发射信号 stateChanged() 。
下面的例子创建一个复选框来切换窗口标题。
'''

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Checkbox')

        # 复选框
        self.cb = QtGui.QCheckBox('Show title', self)
        self.cb.setFocusPolicy(QtCore.Qt.NoFocus)   # 禁用焦点
        self.cb.move(10, 10)
        self.cb.toggle()    # 选中复选框
        self.connect(self.cb, QtCore.SIGNAL('stateChanged(int)'), self.changeTitle)

    def changeTitle(self, value):
        # 复选框被选中，标题为Checkbox；复选框未被选中，标题为空
        if self.cb.isChecked():
            self.setWindowTitle('Checkbox')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
