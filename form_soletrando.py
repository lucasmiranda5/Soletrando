# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_soletrando.ui'
#
# Created: Thu Sep 17 20:24:20 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindowFORM(object):
    def setupUi(self, MainWindowFORM):
        MainWindowFORM.setObjectName(_fromUtf8("MainWindowFORM"))
        MainWindowFORM.resize(800, 605)
        self.centralwidget = QtGui.QWidget(MainWindowFORM)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 30, 461, 51))
        self.plainTextEdit.setStyleSheet(_fromUtf8("width:445px;\n"
"height:45px;\n"
"background:url(\'logo.png\') no-repeat;\n"
"border:0;"))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(30, 110, 251, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet(_fromUtf8("border:0;"))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 180, 541, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 491, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 280, 541, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 281, 41))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 380, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(_fromUtf8("color:#fff;\n"
"background:rgb(3, 191, 0);\n"
"border:0"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineSalvar = QtGui.QLineEdit(self.centralwidget)
        self.lineSalvar.setEnabled(False)
        self.lineSalvar.setGeometry(QtCore.QRect(100, 460, 491, 31))
        self.lineSalvar.setStyleSheet(_fromUtf8("background:transparent;\n"
"border:0"))
        self.lineSalvar.setObjectName(_fromUtf8("lineSalvar"))
        MainWindowFORM.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowFORM)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindowFORM.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowFORM)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowFORM.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowFORM)
        QtCore.QMetaObject.connectSlotsByName(MainWindowFORM)

    def retranslateUi(self, MainWindowFORM):
        MainWindowFORM.setWindowTitle(_translate("MainWindowFORM", "MainWindow", None))
        self.plainTextEdit_2.setPlainText(_translate("MainWindowFORM", "Cadastrar Palavras", None))
        self.groupBox.setTitle(_translate("MainWindowFORM", "Palavra", None))
        self.groupBox_2.setTitle(_translate("MainWindowFORM", "Dificuldade", None))
        self.comboBox.setItemText(0, _translate("MainWindowFORM", "Facil", None))
        self.comboBox.setItemText(1, _translate("MainWindowFORM", "Intermediario", None))
        self.comboBox.setItemText(2, _translate("MainWindowFORM", "Dificil", None))
        self.pushButton.setText(_translate("MainWindowFORM", "SALVAR", None))

