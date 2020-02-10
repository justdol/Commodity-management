# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my2.ui'
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
        self.layoutWidget.setGeometry(QtCore.QRect(0, 510, 491, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(11, 10, 461, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_4.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_4.addWidget(self.pushButton_12)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 361, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        self.pushButton_11.clicked.connect(Form.showUp)
        self.pushButton_2.clicked.connect(Form.showIndex)
        self.pushButton_3.clicked.connect(Form.showRelease)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "商品"))
        self.pushButton_3.setText(_translate("Form", "发布"))
        self.pushButton_4.setText(_translate("Form", "我的"))
        self.pushButton_11.setText(_translate("Form", "我上架的宝贝"))
        self.pushButton_12.setText(_translate("Form", "我购买的宝贝"))
