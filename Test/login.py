# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Index.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(90, 320, 301, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.register_pushButton.sizePolicy().hasHeightForWidth())
        self.register_pushButton.setSizePolicy(sizePolicy)
        self.register_pushButton.setAcceptDrops(False)
        self.register_pushButton.setStyleSheet("QPushButton:disabled{\n"
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
"}\n"
"")
        self.register_pushButton.setObjectName("register_pushButton")
        self.horizontalLayout.addWidget(self.register_pushButton)
        self.Index_pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Index_pushButton.sizePolicy().hasHeightForWidth())
        self.Index_pushButton.setSizePolicy(sizePolicy)
        self.Index_pushButton.setAcceptDrops(False)
        self.Index_pushButton.setStyleSheet("QPushButton:disabled{\n"
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
"}\n"
"")
        self.Index_pushButton.setObjectName("Index_pushButton")
        self.horizontalLayout.addWidget(self.Index_pushButton)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(113, 180, 250, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(40)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.account_lineEdit = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.account_lineEdit.sizePolicy().hasHeightForWidth())
        self.account_lineEdit.setSizePolicy(sizePolicy)
        self.account_lineEdit.setClearButtonEnabled(True)
        self.account_lineEdit.setObjectName("account_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.passWord_lineEdit = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.passWord_lineEdit.sizePolicy().hasHeightForWidth())
        self.passWord_lineEdit.setSizePolicy(sizePolicy)
        self.passWord_lineEdit.setClearButtonEnabled(True)
        self.passWord_lineEdit.setObjectName("passWord_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passWord_lineEdit)

        self.retranslateUi(Form)
        self.account_lineEdit.textChanged['QString'].connect(Form.enable_Index)
        self.passWord_lineEdit.textChanged['QString'].connect(Form.enable_Index)
        self.register_pushButton.clicked.connect(Form.show_register)
        self.Index_pushButton.clicked.connect(Form.Index)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "欢迎来到商品交易平台"))
        self.register_pushButton.setText(_translate("Form", "注册"))
        self.Index_pushButton.setText(_translate("Form", "登录"))
        self.label.setText(_translate("Form", "账    号:"))
        self.label_2.setText(_translate("Form", "密    码:"))

