# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        Form.setAcceptDrops(True)
        self.main_menu_btn = QtWidgets.QPushButton(Form)
        self.main_menu_btn.setGeometry(QtCore.QRect(10, 20, 50, 50))
        self.main_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(253,167,255);\n"
"    border:2px solid rgb(250,218,218);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:4px double rgb(239, 160, 179);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(209, 0, 209);\n"
"}")
        self.main_menu_btn.setCheckable(True)
        self.main_menu_btn.setObjectName("main_menu_btn")
        self.reset_menu_btn = QtWidgets.QPushButton(Form)
        self.reset_menu_btn.setGeometry(QtCore.QRect(80, 80, 50, 50))
        self.reset_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(253,167,255);\n"
"    border:2px solid rgb(250,218,218);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:4px double rgb(239, 160, 179);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(209, 0, 209);\n"
"}")
        self.reset_menu_btn.setCheckable(False)
        self.reset_menu_btn.setObjectName("reset_menu_btn")
        self.exit_menu_btn = QtWidgets.QPushButton(Form)
        self.exit_menu_btn.setGeometry(QtCore.QRect(10, 100, 50, 50))
        self.exit_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(253,167,255);\n"
"    border:2px solid rgb(250,218,218);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:4px double rgb(239, 160, 179);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(209, 0, 209);\n"
"}")
        self.exit_menu_btn.setCheckable(False)
        self.exit_menu_btn.setObjectName("exit_menu_btn")
        self.about_menu_btn = QtWidgets.QPushButton(Form)
        self.about_menu_btn.setGeometry(QtCore.QRect(100, 20, 50, 50))
        self.about_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(253,167,255);\n"
"    border:2px solid rgb(250,218,218);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:4px double rgb(239, 160, 179);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(209, 0, 209);\n"
"}")
        self.about_menu_btn.setCheckable(False)
        self.about_menu_btn.setObjectName("about_menu_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 210, 251, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self._2 = QtWidgets.QFormLayout(self.layoutWidget)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setVerticalSpacing(20)
        self._2.setObjectName("_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self._2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.account_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.account_lineEdit.setClearButtonEnabled(True)
        self.account_lineEdit.setObjectName("account_lineEdit")
        self._2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self._2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.passWord_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.passWord_lineEdit.setClearButtonEnabled(True)
        self.passWord_lineEdit.setObjectName("passWord_lineEdit")
        self._2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passWord_lineEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self._2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.conform_passWord_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.conform_passWord_lineEdit.setClearButtonEnabled(True)
        self.conform_passWord_lineEdit.setObjectName("conform_passWord_lineEdit")
        self._2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.conform_passWord_lineEdit)
        self.reguster_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.reguster_pushButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.reguster_pushButton.sizePolicy().hasHeightForWidth())
        self.reguster_pushButton.setSizePolicy(sizePolicy)
        self.reguster_pushButton.setAcceptDrops(False)
        self.reguster_pushButton.setStyleSheet("QPushButton:disabled{\n"
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
        self.reguster_pushButton.setObjectName("reguster_pushButton")
        self._2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.reguster_pushButton)
        self.reset_menu_btn.raise_()
        self.exit_menu_btn.raise_()
        self.about_menu_btn.raise_()
        self.layoutWidget.raise_()
        self.main_menu_btn.raise_()

        self.retranslateUi(Form)
        self.main_menu_btn.clicked['bool'].connect(Form.show_hid_menue)
        self.about_menu_btn.clicked.connect(Form.about_wc)
        self.reset_menu_btn.clicked.connect(Form.reset)
        self.exit_menu_btn.clicked.connect(Form.exit_pane)
        self.reguster_pushButton.clicked.connect(Form.check_register)
        self.account_lineEdit.textChanged['QString'].connect(Form.enable_registerbtn)
        self.passWord_lineEdit.textChanged['QString'].connect(Form.enable_registerbtn)
        self.conform_passWord_lineEdit.textChanged['QString'].connect(Form.enable_registerbtn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_menu_btn.setText(_translate("Form", "菜单"))
        self.reset_menu_btn.setText(_translate("Form", "重置"))
        self.exit_menu_btn.setText(_translate("Form", "退出"))
        self.about_menu_btn.setText(_translate("Form", "关于"))
        self.label.setText(_translate("Form", "账    号:"))
        self.label_2.setText(_translate("Form", "密    码:"))
        self.label_3.setText(_translate("Form", "确认密码:"))
        self.reguster_pushButton.setText(_translate("Form", "注册"))
