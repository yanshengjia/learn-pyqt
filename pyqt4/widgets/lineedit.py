#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
QLineEdit 窗口组件用来输入或者编辑单行纯文本，有撤销/重做，剪切/粘贴和拖放功能。
下面的例子实现了一个单行编辑器和一个标签。在单行编辑器中键入的文字会立即显示在标签中。
'''



from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.initUI()


    def initUI(self):

        self.label = QtGui.QLabel(self)
        edit = QtGui.QLineEdit(self)

        edit.move(60, 100)
        self.label.move(60, 40)

        self.connect(edit, QtCore.SIGNAL('textChanged(QString)'), self.onChanged)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(250, 200, 350, 250)


    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()


def main():

    app = QtGui.QApplication([])
    exm = Example()
    exm.show()
    app.exec_()


if __name__ == '__main__':
    main()