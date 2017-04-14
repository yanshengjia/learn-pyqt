# !/usr/bin/python
# coding=utf8

# 消息框
# 当我们在编辑器中打开一个文件并且做了一些修改，显示一个消息框来确认这个动作

import sys
from PyQt4 import QtGui

class MessageBox(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message Box')

    # 当我们关闭 QWidget，将会产生一个 QCloseEvent 事件，这里重写了 closeEvent() 来改变组件的行为
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        # 显示一个有2个按钮的消息框，第一个字符串显示在标题栏上，第二个字符串是文本信息，显示在对话框中
        # MacOS 上不显示标题

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QtGui.QApplication(sys.argv)
qb = MessageBox()
qb.show()
app.exit(app.exec_())
