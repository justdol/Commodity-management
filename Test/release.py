# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'release.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 546)
        Form.setMinimumSize(QtCore.QSize(500, 546))
        Form.setMaximumSize(QtCore.QSize(500, 546))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 90, 311, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(25)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Line_price = QtWidgets.QLineEdit(self.layoutWidget)
        self.Line_price.setClearButtonEnabled(True)
        self.Line_price.setObjectName("Line_price")
        self.gridLayout_2.addWidget(self.Line_price, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.Line_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.Line_name.setClearButtonEnabled(True)
        self.Line_name.setObjectName("Line_name")
        self.gridLayout_2.addWidget(self.Line_name, 0, 1, 1, 1)
        self.Line_describe = QtWidgets.QLineEdit(self.layoutWidget)
        self.Line_describe.setClearButtonEnabled(True)
        self.Line_describe.setObjectName("Line_describe")
        self.gridLayout_2.addWidget(self.Line_describe, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.releasebtn = QtWidgets.QPushButton(Form)
        self.releasebtn.setEnabled(False)
        self.releasebtn.setGeometry(QtCore.QRect(340, 330, 151, 61))
        self.releasebtn.setStyleSheet("QPushButton:disabled{\n"
"    background-color:rgb(85, 255, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(255, 170, 127);\n"
"    color:rgb(201,0,94);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(165, 165, 165);\n"
"}")
        self.releasebtn.setObjectName("releasebtn")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 510, 491, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.showIndex)
        self.pushButton_4.clicked.connect(Form.showMy)
        self.releasebtn.clicked.connect(Form.releaseObject)
        self.Line_name.textChanged['QString'].connect(Form.enable_releasebtn)
        self.Line_price.textChanged['QString'].connect(Form.enable_releasebtn)
        self.Line_describe.textChanged['QString'].connect(Form.enable_releasebtn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "描    述:"))
        self.label_5.setText(_translate("Form", "价    格:"))
        self.label_6.setText(_translate("Form", "物品名称:"))
        self.releasebtn.setText(_translate("Form", "发布"))
        self.pushButton_2.setText(_translate("Form", "商品"))
        self.pushButton_3.setText(_translate("Form", "发布"))
        self.pushButton_4.setText(_translate("Form", "我的"))
