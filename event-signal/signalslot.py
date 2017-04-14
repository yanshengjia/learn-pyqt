# !/usr/bin/python
# coding=utf8

# 事件是GUI程序的重要部分，由用户或者系统产生。当我们调用应用的 exec_() 方法，应用进入主循环。主循环获取事件并把它们发往对象。Trolltech引入了独一无二的信号和槽机制。
# 事件是GUI程序的主要部分，所有GUI应用程序都是事件驱动的。应用在它的生命周期中产生的不同事件交互。事件主要由用户产生，但是它们也可以由其他方式产生，如：互联网，窗口管理器，定时器。
# 在事件模型中，由三个参与者：
# * event source(事件来源): 指状态改变的对象，它产生了事件
# * event object(事件对象): 封装了事件元的状态改变
# * event target(事件目标): 事件对象想要通知的对象

# 信号和槽用于对象之间的通讯。 当一个特殊的事件发生时，将发射 信号，槽 可以是任何Python调用，当链接到槽的信号发射，该槽将被调用。


# 这是一个演示 PyQt4 信号与槽的简单例子
# 显示了一个LCD数字和一个滑块，通过拖动滑块来改变LCD的值

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        lcd = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)

        # 连接滑块的 valueChanged() 信号到LCD数字的 display() 槽
        self.connect(slider,  QtCore.SIGNAL('valueChanged(int)'), lcd,
            QtCore.SLOT('display(int)'))
        # connect() 有4个参数， sender 是发送信号的对象， signal 是发射的信号， receiver 是接收信号的对象，最后，slot 是对信号反应的方法。

        self.setWindowTitle('Signal & Slot')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
