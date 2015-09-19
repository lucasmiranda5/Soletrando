# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listar_palavras.ui'
#
# Created: Sat Sep 19 16:35:12 2015
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
        ListaPalavras.resize(570, 660)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ListaPalavras.setWindowIcon(icon)
        self.plainTextEdit = QtGui.QPlainTextEdit(ListaPalavras)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 50, 461, 51))
        self.plainTextEdit.setStyleSheet(_fromUtf8("width:445px;\n"
"height:45px;\n"
"background:url(\'logo.png\') no-repeat;\n"
"border:0;"))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.tableView = QtGui.QTableView(ListaPalavras)
        self.tableView.setGeometry(QtCore.QRect(110, 210, 341, 361))
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.SelectedClicked)
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(ListaPalavras)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(130, 110, 291, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet(_fromUtf8("border:0;"))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.lineEdit = QtGui.QLineEdit(ListaPalavras)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(40, 160, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("border:0;\n"
"background:transparent"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineExcluir = QtGui.QLineEdit(ListaPalavras)
        self.lineExcluir.setEnabled(False)
        self.lineExcluir.setGeometry(QtCore.QRect(50, 580, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineExcluir.setFont(font)
        self.lineExcluir.setStyleSheet(_fromUtf8("border:0;\n"
"background:transparent"))
        self.lineExcluir.setText(_fromUtf8(""))
        self.lineExcluir.setObjectName(_fromUtf8("lineExcluir"))

        self.retranslateUi(ListaPalavras)
        QtCore.QMetaObject.connectSlotsByName(ListaPalavras)

    def retranslateUi(self, ListaPalavras):
        ListaPalavras.setWindowTitle(_translate("ListaPalavras", "Palavras Cadastradas - Soletrando", None))
        self.plainTextEdit_2.setPlainText(_translate("ListaPalavras", "Palavras Cadastradas", None))
        self.lineEdit.setText(_translate("ListaPalavras", "Para excluir alguma palavra clique duas vezes nela", None))

import ico_rc
