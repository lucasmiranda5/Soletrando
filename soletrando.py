# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soletrando.ui'
#
# Created: Sat Sep 19 16:35:16 2015
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

class Ui_Soletrando(object):
    def setupUi(self, Soletrando):
        Soletrando.setObjectName(_fromUtf8("Soletrando"))
        Soletrando.resize(800, 693)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Soletrando.setWindowIcon(icon)
        self.textoBox = QtGui.QPlainTextEdit(Soletrando)
        self.textoBox.setEnabled(False)
        self.textoBox.setGeometry(QtCore.QRect(50, 140, 711, 201))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textoBox.setFont(font)
        self.textoBox.setStyleSheet(_fromUtf8("background:#fff;\n"
"border:1px solid #000;\n"
"color:#000"))
        self.textoBox.setObjectName(_fromUtf8("textoBox"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Soletrando)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 40, 461, 51))
        self.plainTextEdit.setStyleSheet(_fromUtf8("width:445px;\n"
"height:45px;\n"
"background:url(\'logo.png\') no-repeat;\n"
"border:0;"))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.lineEdit = QtGui.QLineEdit(Soletrando)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(500, 360, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("color:#000;\n"
"background:transparent;\n"
"border:0\n"
""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.spinBox = QtGui.QSpinBox(Soletrando)
        self.spinBox.setGeometry(QtCore.QRect(640, 110, 101, 22))
        self.spinBox.setReadOnly(False)
        self.spinBox.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.spinBox.setProperty("value", 20)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.lineEdit_2 = QtGui.QLineEdit(Soletrando)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 110, 121, 22))
        self.lineEdit_2.setStyleSheet(_fromUtf8("color:#000;\n"
"background:transparent;\n"
"border:0;"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.tableView = QtGui.QTableView(Soletrando)
        self.tableView.setGeometry(QtCore.QRect(460, 410, 256, 251))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.groupBox_2 = QtGui.QGroupBox(Soletrando)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 360, 321, 80))
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
        self.pushButton = QtGui.QPushButton(Soletrando)
        self.pushButton.setGeometry(QtCore.QRect(130, 450, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(_fromUtf8("color:#fff;\n"
"background:rgb(3, 191, 0);\n"
"border:0"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Soletrando)
        QtCore.QMetaObject.connectSlotsByName(Soletrando)

    def retranslateUi(self, Soletrando):
        Soletrando.setWindowTitle(_translate("Soletrando", "Soletrando", None))
        self.lineEdit.setText(_translate("Soletrando", "Palavras Soletradas", None))
        self.lineEdit_2.setText(_translate("Soletrando", "Tamanho da fonte:", None))
        self.groupBox_2.setTitle(_translate("Soletrando", "Dificuldade", None))
        self.comboBox.setItemText(0, _translate("Soletrando", "Facil", None))
        self.comboBox.setItemText(1, _translate("Soletrando", "Intermediario", None))
        self.comboBox.setItemText(2, _translate("Soletrando", "Dificil", None))
        self.pushButton.setText(_translate("Soletrando", "SOLETRAR", None))

import ico_rc
