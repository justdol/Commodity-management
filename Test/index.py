# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(500, 546)
        widget.setMinimumSize(QtCore.QSize(500, 546))
        widget.setMaximumSize(QtCore.QSize(500, 546))
        self.verticalLayout = QtWidgets.QVBoxLayout(widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_5 = QtWidgets.QPushButton(widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.release_btn = QtWidgets.QPushButton(widget)
        self.release_btn.setObjectName("release_btn")
        self.horizontalLayout_2.addWidget(self.release_btn)
        self.my_btn = QtWidgets.QPushButton(widget)
        self.my_btn.setObjectName("my_btn")
        self.horizontalLayout_2.addWidget(self.my_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(widget)
        self.release_btn.clicked.connect(widget.show_release)
        self.my_btn.clicked.connect(widget.show_my)
        self.pushButton_5.clicked.connect(widget.search_object)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.lineEdit.setPlaceholderText(_translate("widget", "输入宝贝序号进行购买"))
        self.pushButton_5.setText(_translate("widget", "购买"))
        self.pushButton.setText(_translate("widget", "商品"))
        self.release_btn.setText(_translate("widget", "发布"))
        self.my_btn.setText(_translate("widget", "我的"))
