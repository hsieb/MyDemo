# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(408, 300)
        self.start = QtWidgets.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(20, 210, 93, 28))
        self.start.setObjectName("start")
        self.quit = QtWidgets.QPushButton(Form)
        self.quit.setGeometry(QtCore.QRect(300, 210, 93, 28))
        self.quit.setObjectName("quit")
        self.stop = QtWidgets.QPushButton(Form)
        self.stop.setGeometry(QtCore.QRect(160, 210, 93, 28))
        self.stop.setObjectName("stop")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 291, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 120, 71, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 120, 71, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 120, 71, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 120, 71, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Form)
        self.quit.clicked.connect(Form.slot_quit)
        self.start.clicked.connect(Form.slot_start)
        self.stop.clicked.connect(Form.slot_stop)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.start.setText(_translate("Form", "start"))
        self.quit.setText(_translate("Form", "quit"))
        self.stop.setText(_translate("Form", "stop"))

