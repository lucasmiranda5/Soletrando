import sys
from PyQt4 import QtGui, QtCore
from home import Ui_MainWindow
from form_soletrando import Ui_MainWindowFORM
from listar_palavras import Ui_ListaPalavras
from soletrando import Ui_Soletrando
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import random

class Formulario(QtGui.QMainWindow):
  def __init__(self):
    QtGui.QMainWindow.__init__(self)
    self.ui = Ui_MainWindowFORM()
    self.ui.setupUi(self)
    self.ui.pushButton.clicked.connect(self.salvarForm)

  def salvarForm(self):
     self.ui.lineSalvar.setText("Aguarde! Salvando")
     f = open('palavras.txt','a')
     linha = '\n'+self.ui.lineEdit.text()+';'+self.ui.comboBox.currentText()
     f.write(linha)
     f.close()
     self.ui.lineSalvar.setText("Palavra Salva com Sucesso")

class Soletrando(QtGui.QMainWindow):
  def __init__(self):
    QtGui.QMainWindow.__init__(self)
    self.ui = Ui_Soletrando()
    self.ui.setupUi(self)
    self.ui.pushButton.clicked.connect(self.soletrar)
  sorteadas = []
  sx = 0;
  def soletrar(self):
     f = open('palavras.txt','r')
     ler = f.readlines()
     my_array = []
     x = 0
     b = 0
     total = 0

     
     combo = self.ui.comboBox.currentText()
     for item in ler:
       i = item.split(';')
       i[1] = i[1].replace('\n','')
       my_array.insert(x,[i[0],i[1]])
       x = x + 1       
       if(i[1] == self.ui.comboBox.currentText()):
         b = 1
         total = total + 1
     f.close()
     m = random.randint(0,x-1)
     v = 0
     total2 = 0
     
     for ite in self.sorteadas:
       if(ite[1] == self.ui.comboBox.currentText()):
         total2 = total2  + 1
     if(b == 1):
       v = 0
       t = 0
       while(v == 0):
         tem = 1
         for ite in self.sorteadas:
           print my_array[m][0] not in ite
           print ite
           if(my_array[m][0] in ite):
             tem = 0
         print total2 , ' - ', total
         if(my_array[m][1] == self.ui.comboBox.currentText() and tem == 1 and total2 < total):
           self.ui.textoBox.setPlainText(my_array[m][0])
           v = 1;
           self.sorteadas.insert(self.sx,[my_array[m][0],my_array[m][1]])
           self.sx = self.sx + 1
         elif(total2 >= total):
           self.ui.textoBox.setPlainText("Nao existe mais palavras para esse nivel")
           break
         else:
           m = random.randint(0,x-1)
         
     else:
        self.ui.textoBox.setPlainText("Nao existe palavras para esse nivel")
     print self.sorteadas
           
     
      
     
    

class ListarPalavras(QtGui.QMainWindow):
  def __init__(self):
    QtGui.QMainWindow.__init__(self)
    self.ui = Ui_ListaPalavras()
    self.ui.setupUi(self)
    f = open('palavras.txt','r')
    ler = f.readlines()
    my_array = []
    x = 0;
    for item in ler:
      i = item.split(';')
      my_array.insert(x,[i[0],i[1]])
      x = x + 1
    tablemodel = MyTableModel(my_array, self)
    self.ui.tableView.setModel(tablemodel)
    f.close()
  def salvarForm(self):
     self.ui.lineSalvar.setText("Aguarde! Salvando")
     f = open('palavras.txt','a')
     linha = '\n'+self.ui.lineEdit.text()+';'+self.ui.comboBox.currentText()
     f.write(linha)
     f.close()
     self.ui.lineSalvar.setText("Palavra Salva com Sucesso")

  
class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])
    
class Main(QtGui.QMainWindow):
  def __init__(self):
    QtGui.QMainWindow.__init__(self)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.pushButton_2.clicked.connect(self.charmarForm)
    self.ui.pushButton_3.clicked.connect(self.listarPalavras)
    self.ui.pushButton.clicked.connect(self.soletrando)

  def charmarForm(self):
    programa=Formulario()
    programa.show()
    self.exit()

  def listarPalavras(self):
    programa=ListarPalavras()
    programa.show()
    self.exit()
    
  def soletrando(self):
    programa=Soletrando()
    programa.show()
    self.exit()
    Soletrando
    
app = QtGui.QApplication(sys.argv)
programa=Main()
programa.show()
sys.exit(app.exec_())
  
