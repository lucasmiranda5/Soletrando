import sys
from PyQt4 import QtGui, QtCore
from home import Ui_MainWindow
from form_soletrando import Ui_MainWindowFORM
from listar_palavras import Ui_ListaPalavras
from soletrando import Ui_Soletrando
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import random

class Formulario(QtGui.QDialog):
  def __init__(self, parent=None):
    super(Formulario, self).__init__(parent)
    self.ui = Ui_MainWindowFORM()
    self.ui.setupUi(self)
    self.ui.pushButton.clicked.connect(self.salvarForm)

  def salvarForm(self):
     self.ui.lineSalvar.setText("Aguarde! Salvando")
     f = open('palavras.txt','a')
     f2 = open('palavras.txt','r')
     ler = f2.readlines()
     if(len(ler) > 0):
       linha = '\n'+self.ui.lineEdit.text()+';'+self.ui.comboBox.currentText()
     else:
       linha = self.ui.lineEdit.text()+';'+self.ui.comboBox.currentText()
     f.write(linha)
     f.close()
     self.ui.lineSalvar.setText("Palavra Salva com Sucesso")
class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
class Soletrando(QtGui.QDialog):
  def __init__(self, parent=None):
    super(Soletrando, self).__init__(parent)
    self.ui = Ui_Soletrando()
    self.ui.setupUi(self)
    self.ui.pushButton.clicked.connect(self.soletrar)
    self.ui.spinBox.valueChanged.connect(self.aumentar)
  sorteadas = []
  sx = 0;



  def aumentar(self):
    font = QtGui.QFont()
    font.setPointSize(self.ui.spinBox.value())
    self.ui.textoBox.setFont(font)
  def soletrar(self):
     f = open('palavras.txt','r')
     ler = f.readlines()
     my_array = []
     x = 0
     b = 0
     total = 0
     if(len(self.sorteadas) > 0):
       tablemodel = MyTableModel(self.sorteadas, self)
       self.ui.tableView.setModel(tablemodel)
     else:
       self.ui.tableView.clearSpans()
     
     combo = self.ui.comboBox.currentText()
     if(len(ler) > 0):
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
             if(my_array[m][0] in ite):
               tem = 0

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
     else:
       self.ui.textoBox.setPlainText("Nao existe palavras cadastradas")
class ListarPalavras(QtGui.QDialog):
  ler = []
  def __init__(self, parent=None):
    super(ListarPalavras, self).__init__(parent)
    self.ui = Ui_ListaPalavras()
    self.ui.setupUi(self)
    f = open('palavras.txt','r')
    self.ler = f.readlines()
    my_array = []
    x = 0;
    for item in self.ler:
      i = item.split(';')
      i[1] = i[1].replace('\n','')
      my_array.insert(x,[i[0],i[1]])
      x = x + 1
    if(len(my_array) > 0):
      tablemodel = MyTableModel(my_array, self)
      self.ui.tableView.setModel(tablemodel)
    else:
      self.ui.tableView.clearSpans()
    f.close()
    self.ui.tableView.doubleClicked.connect(self.excluir)
  def excluir(self):
    self.ui.lineExcluir.setText("Aguarde! Excluindo")
    lucas = self.ui.tableView.selectionModel()
    a = lucas.selectedIndexes()
    for aa in a:
      b = aa.row()
      nome = aa.sibling(b, 0).data().toString()
      difi = aa.sibling(b, 1).data().toString()
    x = 0
    my_array = []
    ler2 = []
    arquivo = ''
    for item in self.ler:
      i = item.split(';')
      i[1] = i[1].replace('\n','')

      if((i[0] != nome )):
        if(x == 0):
          arquivo = arquivo + i[0]+";"+i[1]
          ler2.insert(x,i[0]+";"+i[1])
        else:
          arquivo = arquivo + "\n"+ i[0]+";"+i[1]
          ler2.insert(x,i[0]+";"+i[1])
        my_array.insert(x,[i[0],i[1]])        
        x = x+1
    f = open('palavras.txt','w')
    f.write(arquivo)
    f.close()
    self.ler = ler2
    if(len(my_array) > 0):
      tablemodel = MyTableModel(my_array, self)
      self.ui.tableView.setModel(tablemodel)
    else:
      self.ui.tableView.clearSpans()
    self.ui.lineExcluir.setText("Palavra Excluida com sucesso")
      
    
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
    programa.exec_()

  def listarPalavras(self):
    programa=ListarPalavras()
    programa.show()
    programa.exec_()
    
  def soletrando(self):
    programa=Soletrando()
    programa.show()
    programa.exec_()
    Soletrando
    
app = QtGui.QApplication(sys.argv)


app.setApplicationName('MyWindow')
programa=Main()
programa.show()
sys.exit(app.exec_())
  
