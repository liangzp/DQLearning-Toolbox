# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import resource_message_box

class MESSAGE_BOX(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.setObjectName("Dialog")
        self.resize(317, 161)
        self.setStyleSheet("background-image: url(:/image/resource/设定背景.jpg);")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(80, 30, 200, 31))
        self.label.setStyleSheet("font: 12pt \"方正兰亭黑_GB18030\";\n""color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 321, 161))
        self.label_2.setStyleSheet("background-image: url(:/image/resource/设定背景.png);")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(60, 100, 90, 20))
        self.pushButton.setStyleSheet("border-image: url(:/image/resource/设定确定按钮.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 100, 90, 20))
        self.pushButton_2.setStyleSheet("border-image: url(:/image/resource/设定取消按钮.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "请问是否需要保存记录？"))


