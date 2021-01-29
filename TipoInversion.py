#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
import psycopg2
import sys
import pprint
import Base_de_datos
import MergeSort
from time import time
import Arbol
import Dijkstra

class Tipo_inversion:
    def __init__(self,id=None,nombre=None,porcentaje_utilidad=None,tasa_pago=None):
            self.id=id
            self.nombre = nombre
            self.porcentaje_utilidad = porcentaje_utilidad
            self.tasa_pago =tasa_pago
    def ingresar(self):
        self.ventanaIngresar=Toplevel()
        self.ventanaIngresar.geometry("570x400")
        self.ventanaIngresar.title("Tipo de inversion")
        img = PhotoImage(file="C:/Users/checo/Desktop/41-INVERSION-MEDIOS-DIGITALES.png")
        imagen= Label(self.ventanaIngresar, image=img)
        imagen.pack()
        Label(self.ventanaIngresar, text="Tipo de inversion",font=("Cambria",14)).place(x=5,y=0)
        Label(self.ventanaIngresar, text="Id: ",font=("Cambria",11)).place(x=0,y=30)  
        Label(self.ventanaIngresar, text="Nombre: ",font=("Cambria",11)).place(x=0,y=60)
        Label(self.ventanaIngresar, text="Porcentaje de utilidad: ",font=("Cambria",11)).place(x=0,y=90)
        Label(self.ventanaIngresar, text="tasa de pago: ",font=("Cambria",11)).place(x=0,y=120)

        self.id=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.id).place(x=30,y=30)
        self.nombre=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.nombre).place(x=65,y=60)
        self.porcentaje_utilidad=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.porcentaje_utilidad).place(x=150,y=90)
        self.tasa_pago=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.tasa_pago).place(x=90,y=120)
        
        Button(self.ventanaIngresar,text="Guardar",font=("Cambria",11),
                   width=15,command=self.BD).place(x=420,y=5)
        
        Button(self.ventanaIngresar,text="Dijkstra",font=("Cambria",11),
                   width=15, command=self.dijkstra).place(x=420,y=365)
                   
        Button(self.ventanaIngresar,text="Mostrar",font=("Cambria",11),
                     width=15, command=self.Mostrar).place(x=0,y=365)
                     
        Button(self.ventanaIngresar,text="Ordenar",font=("Cambria",11),
                     width=15,command=self.Ordenamiento).place(x=140,y=365)
                     
        Button(self.ventanaIngresar,text="Buscar",font=("Cambria",11),
                     width=15,command=self.Busqueda).place(x=280,y=365)
        
        self.ventanaIngresar.mainloop()  
        
    def BD(self):
        conectar=Base_de_datos.BaseDeDatos()
        comando="INSERT INTO tipo_inversion(id,nombre,porcentaje_utilidad,tasa_pago) VALUES('"+self.id.get()+"','"+self.nombre.get()+"','"+self.porcentaje_utilidad.get()+"','"+self.tasa_pago.get()+"')"
        print(comando)
        conectar.cursor.execute(comando)
    def Ordenamiento(self):
        comando="SELECT porcentaje_utilidad FROM tipo_inversion;"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        rows= conectar.cursor.fetchall()
        tiempo_inicial = time()
        ordenar=MergeSort.merge_sort(rows)
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        print(ordenar)
        #print("El tiempo de ejecucion fue de:",tiempo_ejecucion)
    def Mostrar(self):
        comando="SELECT * FROM tipo_inversion;"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        Scroll=Scrollbar(self.ventanaIngresar, orient=VERTICAL)
        self.listbox=Listbox(self.ventanaIngresar, font=("Cambria",9), borderwidth=0, yscrollcommand=Scroll.set,height=11,relief="sunken",width=70)
        self.listbox.place(x=5, y=180)
        Scroll.config(command=self.listbox.yview)
        Scroll.pack(side=RIGHT, fill=Y)
        for dato1, dato2 in enumerate(conectar.cursor.fetchall()):
            self.listbox.insert(0, "Id: {}".format(dato2[0]))
            self.listbox.insert(1, "Nombre: {}".format(dato2[1]))
            self.listbox.insert(2, "porcentaje de utilidad: {}".format(dato2[2]))
            self.listbox.insert(3, "tasa de pago: {}".format(dato2[3]))
            self.listbox.insert(4, " ")
    def Busqueda(self):
        self.ingresarArbol()
        self.palabra=None
        self.ventanaBusqueda=Toplevel()
        self.ventanaBusqueda.geometry("265x168")
        self.ventanaBusqueda.title("Buscar")
        Label(self.ventanaBusqueda, text="Ingresa el id del tipo de inversion",font=("Calibri Light",14)).place(x=5,y=0)
        self.palabra=StringVar()
        Entry(self.ventanaBusqueda, textvariable=self.palabra).place(x=70,y=30)
        Button(self.ventanaBusqueda,text="Buscar",font=("Cambria",11),
                   width=10,command=self.Buscar).place(x=90,y=60)
        self.listbox=Listbox(self.ventanaBusqueda, font=("Cambria",11), borderwidth=0, height=4,relief="sunken",width=30)
        self.listbox.place(x=7, y=95)
    def Buscar(self):
        comando="SELECT * FROM tipo_inversion where id='"+self.palabra.get()+"';"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        if self.palabra.get() not in self.id.get():
            self.listbox.insert(0, "No existe registro con ese id")
        for dato1, dato2 in enumerate(conectar.cursor.fetchall()):
            self.listbox.insert(0, "Id: {}".format(dato2[0]))
            self.listbox.insert(1, "Nombre: {}".format(dato2[1]))
            self.listbox.insert(2, "porcentaje de utilidad: {}".format(dato2[2]))
            self.listbox.insert(3, "tasa de pago: {}".format(dato2[3]))
    def ingresarArbol(self):
        self.dato2=None 
        self.arbol=Arbol.ArbolBinarioBusqueda()
        comando="SELECT * FROM tipo_inversion;"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        tiempo_inicial = time()
        for dato1, self.dato2 in enumerate(conectar.cursor.fetchall()): 
            self.arbol.__setitem__(self.dato2[0], self.dato2)
            print(self.arbol.__getitem__(self.dato2[0]))
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        #print("El tiempo de ejecucion fue de:",tiempo_ejecucion)    
    def ArbolBusqueda(self):
        if not  self.arbol.__getitem__(self.palabra.get()):
            self.listbox.insert(0, "No existe registro con ese id")
        
        tiempo_inicial = time()
        #self.listbox.insert(0, self.arbol.__getitem__(self.palabra.get()))
        print(self.arbol.__getitem__(self.palabra.get()))
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        print("El tiempo de busqueda fue de:",tiempo_ejecucion)  
    def dijkstra(self):
        comando="SELECT * FROM tipo_inversion CROSS JOIN pago_interes;"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        self.g=Dijkstra.Graph()
        for dato1, self.dato2 in enumerate(conectar.cursor.fetchall()):
            self.g.add_node(self.dato2[5])
        for dato1, self.dato2 in enumerate(conectar.cursor.fetchall()):
            self.g.add_edge(self.dato2[5], self.dato2[5], self.dato2[7])
        self.palabra=None 
        self.ventanaBusqueda=Toplevel()
        self.ventanaBusqueda.geometry("265x298")
        self.ventanaBusqueda.title("Dijkstra")
        Label(self.ventanaBusqueda, text="Id de inversion",font=("Calibri Light",14)).place(x=5,y=0)
        self.palabra=StringVar()
        Entry(self.ventanaBusqueda, textvariable=self.palabra).place(x=70,y=30)
        Button(self.ventanaBusqueda,text="Buscar",font=("Cambria",11),
                   width=10, command=self.funcionDijkstra).place(x=70,y=90)
                   
    def funcionDijkstra(self):
        buscar=Dijkstra
        print(buscar.dijsktra(self.g, self.palabra.get()))