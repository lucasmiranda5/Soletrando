# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soletrando.ui'
#
# Created: Thu Sep 17 20:31:09 2015
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
        Soletrando.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Soletrando)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 50, 461, 51))
        self.plainTextEdit.setStyleSheet(_fromUtf8("width:445px;\n"
"height:45px;\n"
"background:url(\'logo.png\') no-repeat;\n"
"border:0;"))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 390, 541, 80))
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
        self.pushButton.setGeometry(QtCore.QRect(300, 480, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(_fromUtf8("color:#fff;\n"
"background:rgb(3, 191, 0);\n"
"border:0"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textoBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.textoBox.setEnabled(False)
        self.textoBox.setGeometry(QtCore.QRect(50, 150, 711, 201))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textoBox.setFont(font)
        self.textoBox.setStyleSheet(_fromUtf8("background:#fff;\n"
"border:1px solid #000;\n"
"color:#000"))
        self.textoBox.setObjectName(_fromUtf8("textoBox"))
        Soletrando.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Soletrando)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Soletrando.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Soletrando)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Soletrando.setStatusBar(self.statusbar)

        self.retranslateUi(Soletrando)
        QtCore.QMetaObject.connectSlotsByName(Soletrando)

    def retranslateUi(self, Soletrando):
        Soletrando.setWindowTitle(_translate("Soletrando", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("Soletrando", "Dificuldade", None))
        self.comboBox.setItemText(0, _translate("Soletrando", "Facil", None))
        self.comboBox.setItemText(1, _translate("Soletrando", "Intermediario", None))
        self.comboBox.setItemText(2, _translate("Soletrando", "Dificil", None))
        self.pushButton.setText(_translate("Soletrando", "GERAR", None))

