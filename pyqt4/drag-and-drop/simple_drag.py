#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
在下面的例子中，有一个 QLineEdit 和一个 QPushButton 。
我们将从单行编辑器中拖动纯文本到按钮上。
"""

import sys
from PyQt4 import QtGui

# 为了把文本放到 QPushButton 窗口组件上，必须重新实现一些方法。
# 我们创建自己的 Button 类，从 QPushButton 继承。
class Button(QtGui.QPushButton):

    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

        self.setAcceptDrops(True)   # 为窗口组件设置可以接受 Drop 事件

    # 重新实现 dragEnterEvent() 方法。
    # 接受的数据类型，在本例中是纯文本。
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    # 重新实现 dropEvent() 方法中，我们定义在拖入事件中处理什么任务。
    # 这里我们修改按钮的文字。
    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        edit = QtGui.QLineEdit('', self)
        edit.setDragEnabled(True)   # QLineEdit 窗口组件有内置拖动操作支持，我们需要做的是调用 setDragEnabled 方法并激活它。
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple Drag & Drop')
        self.setGeometry(300, 300, 300, 150)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()