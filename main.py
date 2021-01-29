import sys , os
from PyQt4 import QtCore, QtGui
from aerolinea import Ui_formMainWindow
import networkx as nx
import matplotlib.pyplot as plt
from kruskalPrim import minimum_spanning_edges

class Principal(QtGui.QMainWindow):
	def __init__(self):
		self.datos = list()
		self.g = nx.Graph()
		QtGui.QMainWindow.__init__(self)
		self.ui=Ui_formMainWindow()
		self.ui.setupUi(self)
		self.msg = QtGui.QMessageBox()
		self.ui.agregarPushButton.clicked.connect(self.agregar_nod)
		self.ui.registrarPushButton.clicked.connect(self.agregar_reg)
		self.ui.mostrarPushButton.clicked.connect(self.mostrar_reg)
		self.ui.buscarPushButton.clicked.connect(self.buscar_reg)
		self.ui.modificarPushButton.clicked.connect(self.modificar_reg)
		self.ui.ordenarPushButton.clicked.connect(self.ordenar_reg)
		self.ui.profundidadPushButton.clicked.connect(self.profundidad)
		self.ui.anchuraPushButton.clicked.connect(self.anchura)
		self.ui.kruskalPushButton.clicked.connect(self.kruskal)
		self.ui.primPushButton.clicked.connect(self.prim)

	def agregar_nod(self):
		self.g.add_node(self.ui.nodoLineEdit.text())
		self.ui.nodoLineEdit.clear()

	def agregar_reg(self): 
		self.datos.append(self.ui.origenLineEdit.text())
		self.datos.append(self.ui.destinoLineEdit.text())
		self.datos.append(self.ui.distanciaLineEdit.text())
		self.datos.append(self.ui.salidaDateEdit.text())
		self.datos.append(self.ui.arriboDateEdit.text())
		self.guardar_reg()
		origen = self.ui.origenLineEdit.text()
		destino = self.ui.destinoLineEdit.text()
		distancia = float(self.ui.distanciaLineEdit.text()) # pediente
		self.ui.origenLineEdit.clear()
		self.ui.destinoLineEdit.clear()
		self.ui.distanciaLineEdit.clear()
		self.g.add_edge(origen,destino,weight=distancia)
		nx.draw(self.g,with_labels=True,node_size=600,node_color='c')
		plt.show()
				
	def mostrar_reg(self):
		self.cargar_reg()
		c = 0
		v = 0
		while v < len(self.datos)-2:
			if self.ui.mostrarTableWidget.rowCount() < c+1:
				self.ui.mostrarTableWidget.insertRow(self.ui.mostrarTableWidget.rowCount()) # Inserta columnas si es necesario
			self.ui.mostrarTableWidget.setItem(c,0,QtGui.QTableWidgetItem(self.datos[v])) # Inserta los items
			self.ui.mostrarTableWidget.setItem(c,1,QtGui.QTableWidgetItem(self.datos[v+1]))
			self.ui.mostrarTableWidget.setItem(c,2,QtGui.QTableWidgetItem(self.datos[v+2]))
			self.ui.mostrarTableWidget.setItem(c,3,QtGui.QTableWidgetItem(self.datos[v+3]))
			self.ui.mostrarTableWidget.setItem(c,4,QtGui.QTableWidgetItem(self.datos[v+4]))
			c += 1
			v += 5

	def buscar_reg(self):
		self.cargar_reg()
		try:
			c = self.datos.index(self.ui.buscarLineEdit.text())
			if self.ui.modificarTableWidget.rowCount() == 0:
				self.ui.modificarTableWidget.insertRow(self.ui.modificarTableWidget.rowCount()) # Inserta columnas si es necesario
			self.ui.modificarTableWidget.setItem(0,0,QtGui.QTableWidgetItem(self.datos[c])) # Inserta los items
			self.ui.modificarTableWidget.setItem(0,1,QtGui.QTableWidgetItem(self.datos[c+1]))
			self.ui.modificarTableWidget.setItem(0,2,QtGui.QTableWidgetItem(self.datos[c+2]))
			self.ui.modificarTableWidget.setItem(0,3,QtGui.QTableWidgetItem(self.datos[c+3]))
			self.ui.modificarTableWidget.setItem(0,4,QtGui.QTableWidgetItem(self.datos[c+4]))
			return c
		except ValueError:
			self.msg.information(self,"informativo","Valor no encontrado")

	def modificar_reg(self):
		c = self.datos.index(self.ui.buscarLineEdit.text())
		d = ','
		actual = self.datos[c]+d+self.datos[c+1]+d+self.datos[c+2]+d+self.datos[c+3]+d+self.datos[c+4]+d
		if self.ui.modOrigenLineEdit.isModified(): #check out!
			self.datos[c] = self.ui.modOrigenLineEdit.text()
		if self.ui.modDestinoLineEdit.isModified(): #---->
			self.datos[c+1] = self.ui.modDestinoLineEdit.text()
		if self.ui.modDistanciaLineEdit.isModified(): #--->
			self.datos[c+2] = self.ui.modDistanciaLineEdit.text()
		self.datos[c+3] = self.ui.modSalidaDateEdit.text()
		self.datos[c+4] = self.ui.modArriboDateEdit.text()
		self.ui.modOrigenLineEdit.clear()
		self.ui.modDestinoLineEdit.clear()
		self.ui.modDistanciaLineEdit.clear()
		auxiliar = 'auxiliar.txt'
		nombre_archivo = 'delimitadores.txt'
		cambio = self.datos[c]+d+self.datos[c+1]+d+self.datos[c+2]+d+self.datos[c+3]+d+self.datos[c+4]+d
		try:
			f = open(nombre_archivo,'r')
			f2 = open(auxiliar,'w')
			cadena = f.read()
			remplazo = cadena.replace(actual,cambio)
			f2.write(remplazo	)
		except:
			self.msg.information(self,"informativo","Valores no escritos")			
		finally:
			f.close()	
			f2.close()
			os.remove(nombre_archivo)
			os.rename(auxiliar,nombre_archivo)

	def guardar_reg(self):
		d = ','
		try:
			nombre_archivo = 'delimitadores.txt'
			f = open(nombre_archivo,'a')
			f.write(self.ui.origenLineEdit.text() + d)
			f.write(self.ui.destinoLineEdit.text() + d)
			f.write(self.ui.distanciaLineEdit.text() + d)
			f.write(self.ui.salidaDateEdit.text() + d)
			f.write(self.ui.arriboDateEdit.text() + d)
		except:
			self.msg.information(self,"informativo","Valores no guardados")
		finally:
			f.close()

	def cargar_reg(self):
		d = ','
		try:
			nombre_archivo = 'delimitadores.txt'
			f = open(nombre_archivo,'r')
			lis = f.read()
			l = lis.split(d)
			i = 0
			del self.datos[0:]
			while i < len(l)-1:
				self.datos.append(l[i])
				i += 1
				self.datos.append(l[i])
				i += 1
				self.datos.append(l[i])
				i += 1
				self.datos.append(l[i])
				i += 1
				self.datos.append(l[i])
				i += 1
		except:
			self.msg.information(self,"informativo","Valores no cargados")
		finally:
			f.close()

	def quicksort(self,lista_reg,lista,izq,der):
	    i=izq
	    j=der
	    x=lista[int((izq + der)/2)]
	 
	    while( i <= j ):
	        while lista[i]<x and j<=der:
	            i=i+1
	        while x<lista[j] and j>izq:
	            j=j-1
	        if i<=j:
	            aux = lista[i]; lista[i] = lista[j]; lista[j] = aux
	            aux2 = lista_reg[i]; lista_reg[i] = lista_reg[j]; lista_reg[j] = aux2
	            i=i+1;  j=j-1;
	 
	        if izq < j:
	            self.quicksort(lista_reg, lista, izq, j )
	    if i < der:
	        self.quicksort(lista_reg, lista, i, der )
 
	def ordenar_reg(self):
		self.cargar_reg()
		d = ','
		i = 0
		j = 5
		nl = list()
		nl2 = list()
		if(self.ui.origenRadioButton.isChecked() == True):
			while i < len(self.datos):
				nl.append(self.datos[i])
				i +=5
			i = 0
			while i < len(self.datos):
				nl2.append(self.datos[i:j])
				i += 5
				j += 5
			self.quicksort(nl2,nl,0,len(nl)-1)
		i = 0
		if(self.ui.destinoRadioButton.isChecked() == True):
			while i < len(self.datos):
				nl.append(self.datos[i+1])
				i +=5
			i = 0
			while i < len(self.datos):
				nl2.append(self.datos[i:j])
				i += 5
				j += 5
			self.quicksort(nl2,nl,0,len(nl)-1)
		i = 0
		if(self.ui.distanciaRadioButton.isChecked() == True):
			while i < len(self.datos):
				nl.append(self.datos[i+2])
				i +=5
			i = 0
			while i < len(self.datos):
				nl2.append(self.datos[i:j])
				i += 5
				j += 5
			self.quicksort(nl2,nl,0,len(nl)-1)
		i = 0
		if(self.ui.salidaRadioButton.isChecked() == True):
			while i < len(self.datos):
				nl.append(self.datos[i+3])
				i +=5
			i = 0
			while i < len(self.datos):
				nl2.append(self.datos[i:j])
				i += 5
				j += 5
			self.quicksort(nl2,nl,0,len(nl)-1)
		i = 0
		if(self.ui.arriboRadioButton.isChecked() == True):
			while i < len(self.datos):
				nl.append(self.datos[i+4])
				i +=5
			i = 0
			while i < len(self.datos):
				nl2.append(self.datos[i:j])
				i += 5
				j += 5
			self.quicksort(nl2,nl,0,len(nl)-1)
		i = 0
		try:
			nombre_archivo = 'auxiliar.txt'
			a = open(nombre_archivo,'w')
			while i < len(nl2):		
					nl2[i] = d.join(nl2[i])
					i += 1
			a.write(d.join(nl2) + d)
		except:
			self.msg.information(self,"informativo","Valores no guardados")
		finally:
			a.close()
			os.remove("delimitadores.txt")
			os.rename(nombre_archivo,"delimitadores.txt")

	def anchura(self):
		pila = list()
		tuplas= list()
		nodos = self.g.edges()
		i = 0
		j = 0
		band = False
		pila.append(nodos[0][0]) # <----valor elegido
		print("ANCHURA")
		print("pila: ",pila)
		while j < len(pila):
			while i < len(nodos):
				print("nodos: ",nodos)
				print("tupla: ",nodos[i])
				print("si? ",pila[j]," esta en ",nodos[i])
				if pila[j] in nodos[i]: # checa si el elemento existe en cada tupla.
					band = True
					print("encontrado!")
					if nodos[i].index(pila[j]) == 0: # si el elemento existe en a primera posicion.
						pila.append(nodos[i][1])
						print("eliminando: ",nodos[i])
						tuplas.append(nodos[i])
						nodos.remove(nodos[i])
					else:
						pila.append(nodos[i][0])
						print("eliminado: ",nodos[i])
						tuplas.append(nodos[i])
						nodos.remove(nodos[i])
						i = 0
				i+=1
				if band is True:
					band = False
					i-=1
					continue
				
			j+=1
			i=0
		print("nodos despues: ",nodos)
		print("tuplas: ",tuplas)
		print("pila despues: ",pila) # llamar al grafo para mostrar!
		p = nx.Graph()
		p.add_nodes_from(self.g.nodes()) # agrega todos los nodos.
		p.add_edges_from(tuplas) # camino anchura.
		nx.draw(p,with_labels=True,node_size=600,node_color='c')
		plt.show()


	def profundidad(self):
		cola = list()
		tuplas= list()
		nodos = self.g.edges()
		i = 0
		j = 0
		band = False
		cola.append(nodos[0][0]) # <----valor elegido
		print("PROFUNDIDAD")
		print("cola: ",cola)
		while j < len(cola):
			while i < len(nodos):
				print("nodos: ",nodos)
				print("tupla: ",nodos[i])
				print("si? ",cola[j]," esta en ",nodos[i])
				if cola[j] in nodos[i]: # checa si el elemento existe en cada tupla.
					band = True
					print("encontrado!")
					if nodos[i].index(cola[j]) == 0: # si el elemento existe en a primera posicion.
						cola.insert(0,nodos[i][1])
						print("eliminando: ",nodos[i])
						tuplas.append(nodos[i])
						nodos.remove(nodos[i])
					else:
						cola.insert(0,nodos[i][0])
						print("eliminado: ",nodos[i])
						tuplas.append(nodos[i])
						nodos.remove(nodos[i])
						i = 0
					j=0
				i+=1
				if band is True:
					band = False
					i-=1
					continue
				
			j+=1
			i=0
		print("nodos despues: ",nodos)
		print("tuplas: ",tuplas)
		print("cola despues: ",cola) # llamar al grafo para mostrar!
		p = nx.Graph()
		p.add_nodes_from(self.g.nodes()) # agrega todos los nodos.
		p.add_edges_from(tuplas) # camino anchura.
		nx.draw(p,with_labels=True,node_size=600,node_color='c')
		plt.show()

	def kruskal(self):
		p = nx.Graph()
		p.add_nodes_from(self.g.nodes()) # agrega todos los nodos.
		mst = minimum_spanning_edges(self.g, algorithm='kruskal', data=False)
		edgelist = list(mst)
		print("KRUSKAL")
		print(edgelist)
		p.add_edges_from(edgelist) # camino anchura.
		nx.draw(p,with_labels=True,node_size=600,node_color='c')
		plt.show()

	def prim(self):
		p = nx.Graph()
		p.add_nodes_from(self.g.nodes()) # agrega todos los nodos.
		mst = minimum_spanning_edges(self.g, algorithm='prim', data=False)
		print("PRIM")
		edgelist = list(mst)
		print(edgelist)
		p.add_edges_from(edgelist) # camino anchura.
		nx.draw(p,with_labels=True,node_size=600,node_color='c')
		plt.show()		


def main():
	app = QtGui.QApplication(sys.argv)
	ventana = Principal() 
	ventana.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()