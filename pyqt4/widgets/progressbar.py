#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
进度条使用来处理长时间任务的窗口组件，当看到它的动画时，用户就知道我们的任务正在进行中。
在PyQt4工具包中， QProgressBar 窗口组件提供水平或者垂直的进度条。
任务被分成一些阶段。
程序员可以为进度条设置最小值和最大值。默认是0，99.
下面的例子中有一个水平进度条和一个按钮，按钮开始或结束进度条。
'''

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()

    def initUI(self):

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.button = QtGui.QPushButton('Start', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(40, 80)

        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.doAction)

        self.timer = QtCore.QBasicTimer()   # 定时器对象激活进度条
        self.step = 0

        self.setWindowTitle('ProgressBar')
        self.setGeometry(300, 300, 250, 150)

    # 通过 start() 方法加载定时器事件
    def timerEvent(self, event):

        if self.step >= 100:
            self.timer.stop()
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(100, self)
            self.button.setText('Stop')


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()