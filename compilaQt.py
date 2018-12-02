#!/usr/bin/python
import numpy as np
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QPushButton, QVBoxLayout, QListWidget, QListWidgetItem, QTableView
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

Ui_MainWindow, QtBaseClass = uic.loadUiType("interface.ui")

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        #super(QMainWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)                   
        
        tableItem 	= QTableWidgetItem()
        
        self.table.setWindowTitle("QTableWidget Example @pythonspot.com")
        self.table.resize(400, 250)
        self.table.setRowCount(100)
        self.table.setColumnCount(3)        
        self.table.setHorizontalHeaderLabels(("Nome Disciplina", "Carga Horaria", "Nota"))
                
	def imprime_formatado(nome_disciplina, tamanho, argumento):
		
		for i in range(int(tamanho)-int(len((nome_disciplina)))):
			print argumento,
			sys.stdout.write("")
		return

	def calcula_IA(nota, carga_horaria):

		return float(nota)*float(carga_horaria)    
				
	codigo_disciplina = []
	nome_disciplina = []
	carga_horaria = []
	nota = []

	arq = open("Historico.dat", "r")	
	codigo_disciplina, nome_disciplina, carga_horaria, nota = np.loadtxt(arq, delimiter=',', usecols=(0, 1, 2, 3), unpack=True, dtype=str)

	IA = 0.0
	IAA = 0.0
	acumulado = 0.0
	acumulado_IAA = 0.0
	tamanho_espacamento = 0.0
	
	lista_codigo_disciplinas = []

	for i in range (len(codigo_disciplina)):
		if( int(len(nome_disciplina[i])) > int(tamanho_espacamento) ):
			tamanho_espacamento = len(nome_disciplina[i])	
	
	self.table.setRowCount(len(codigo_disciplina))
	
	for i in range (len(codigo_disciplina)):

		if( nome_disciplina[i] != '0' and carga_horaria[i] != '0' and nota[i] != '0' ):			
			
			lista_codigo_disciplinas.append(str(codigo_disciplina[i]))
			self.table.setItem(i-1,0, QTableWidgetItem(str(nome_disciplina[i])))
			self.table.setItem(i-1,1, QTableWidgetItem(str(int(carga_horaria[i]))))
			self.table.setItem(i-1,2, QTableWidgetItem(str(float(nota[i]))))	
					
		else:

			IAA = float(IAA) + round(float(IA),2)	
			acumulado_IAA = float(acumulado_IAA) + round(float(acumulado),2)
			if(i != 0 ):			
				
				lista_codigo_disciplinas.append(str(" "))
				self.table.setItem(i-1,0, QTableWidgetItem("IA: " + str(round(float(IA)/float(acumulado),2))))
				self.table.setItem(i-1,1, QTableWidgetItem("IAA: " + str(round(float(IAA)/float(acumulado_IAA),2))))
				
				IA = 0.0
				acumulado = 0.0 		

		#estatistica IA e IAA				
		IA = float(IA)+float(calcula_IA(nota[i], carga_horaria[i]))
		acumulado = float(acumulado)+float(carga_horaria[i])
		
	lista_codigo_disciplinas.append(str(" "))	
	self.table.setVerticalHeaderLabels(lista_codigo_disciplinas)
		
	IAA = float(IAA) + round(float(IA),2)	
	acumulado_IAA = float(acumulado_IAA) + round(float(acumulado),2)	
	
	self.table.setItem(len(lista_codigo_disciplinas)-1,0, QTableWidgetItem("IA: " + str(round(float(IA)/float(acumulado),2))))
	self.table.setItem(len(lista_codigo_disciplinas)-1,1, QTableWidgetItem("IAA: " + str(round(float(IAA)/float(acumulado_IAA),2))))
	
	self.table.show()        
	


if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = MainWindow()
	main.show()
	sys.exit(app.exec_())
