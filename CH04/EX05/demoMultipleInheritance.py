# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoMultipleInheritance.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(382, 322)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(140, 60, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditName.setFont(font)
        self.lineEditName.setObjectName("lineEditName")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(150, 280, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ButtonClickMe.setFont(font)
        self.ButtonClickMe.setObjectName("ButtonClickMe")
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(140, 20, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditCode.setFont(font)
        self.lineEditCode.setObjectName("lineEditCode")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditHistoryMarks = QtWidgets.QLineEdit(Dialog)
        self.lineEditHistoryMarks.setGeometry(QtCore.QRect(140, 100, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditHistoryMarks.setFont(font)
        self.lineEditHistoryMarks.setObjectName("lineEditHistoryMarks")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditGeographyMarks = QtWidgets.QLineEdit(Dialog)
        self.lineEditGeographyMarks.setGeometry(QtCore.QRect(140, 140, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditGeographyMarks.setFont(font)
        self.lineEditGeographyMarks.setObjectName("lineEditGeographyMarks")
        self.lineEditPercentage = QtWidgets.QLineEdit(Dialog)
        self.lineEditPercentage.setEnabled(False)
        self.lineEditPercentage.setGeometry(QtCore.QRect(140, 220, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditPercentage.setFont(font)
        self.lineEditPercentage.setObjectName("lineEditPercentage")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEditTotal = QtWidgets.QLineEdit(Dialog)
        self.lineEditTotal.setEnabled(False)
        self.lineEditTotal.setGeometry(QtCore.QRect(140, 180, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditTotal.setFont(font)
        self.lineEditTotal.setObjectName("lineEditTotal")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Student Name"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
        self.label_2.setText(_translate("Dialog", "Student Code"))
        self.label_3.setText(_translate("Dialog", "History Marks"))
        self.label_4.setText(_translate("Dialog", "Geography Marks"))
        self.label_5.setText(_translate("Dialog", "Percentage"))
        self.label_6.setText(_translate("Dialog", "Total"))
