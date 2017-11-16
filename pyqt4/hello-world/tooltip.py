# !/usr/bin/python
# coding=utf8

# 为一个 QWidget 窗口组件显示工具提示

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Tooltip(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)    # 从屏幕上(300, 300)位置开始(作为左上角的点)，画一个250*150的矩形界面(宽250，高150)
        self.setWindowTitle('Tooltip')          # 设置标题

        self.setToolTip('This is a <b>QWidget</b> widgt.')  # 设置『提示』
        QtGui.QToolTip.setFont(QtGui.QFont('Monaco', 12))

app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())
