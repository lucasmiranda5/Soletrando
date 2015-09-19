# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listar_palavras.ui'
#
# Created: Thu Sep 17 18:32:49 2015
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

class Ui_ListaPalavras(object):
    def setupUi(self, ListaPalavras):
        ListaPalavras.setObjectName(_fromUtf8("ListaPalavras"))
        ListaPalavras.resize(800, 600)
        self.centralwidget = QtGui.QWidget(ListaPalavras)
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
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 100, 291, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet(_fromUtf8("border:0;"))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 160, 681, 361))
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        ListaPalavras.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ListaPalavras)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ListaPalavras.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ListaPalavras)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ListaPalavras.setStatusBar(self.statusbar)

        self.retranslateUi(ListaPalavras)
        QtCore.QMetaObject.connectSlotsByName(ListaPalavras)

    def retranslateUi(self, ListaPalavras):
        ListaPalavras.setWindowTitle(_translate("ListaPalavras", "MainWindow", None))
        self.plainTextEdit_2.setPlainText(_translate("ListaPalavras", "Palavras Cadastradas", None))

