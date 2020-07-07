#! usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoProgressBar import *
import time


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonStart.clicked.connect(self.updateBar)
        self.ui.progressBar.setValue(0)
        self.show()

    def updateBar(self):
        x = 0
        while x < 100:
            x += 0.00005
            self.ui.progressBar.setValue(x)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
