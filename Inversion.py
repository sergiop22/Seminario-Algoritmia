#!/usr/bin/python
#This Python file uses the following encoding: utf-8
# coding=<encoding name>
from tkinter import *
from time import time
import psycopg2
import sys
import pprint
import MergeSort
import Base_de_datos
import Grafo
import random

class Inversion:
    def __init__(self,id=None,fecha=None,tiempo_dias=None,id_cliente=None,importe=None):
            self.id=id
            self.fecha = fecha
            self.tiempo_dias = tiempo_dias
            self.id_cliente = id_cliente
            self.importe = importe
    def ingresar(self):
        self.ventanaIngresar=Toplevel()
        self.ventanaIngresar.geometry("570x400")
        self.ventanaIngresar.title("Inversion")
        img = PhotoImage(file="C:/Users/checo/Desktop/41-INVERSION-MEDIOS-DIGITALES.png")
        imagen= Label(self.ventanaIngresar, image=img)
        imagen.pack()
        Label(self.ventanaIngresar, text="Inversion",font=("Cambria",14)).place(x=5,y=0)
        Label(self.ventanaIngresar, text="Id: ",font=("Cambria",11)).place(x=0,y=30)
        Label(self.ventanaIngresar, text="Fecha: ",font=("Cambria",11)).place(x=0,y=60)
        Label(self.ventanaIngresar, text="Dias: ",font=("Cambria",11)).place(x=0,y=90)
        Label(self.ventanaIngresar, text="Id del cliente: ",font=("Cambria",11)).place(x=0,y=120)
        Label(self.ventanaIngresar, text="Importe: ",font=("Cambria",11)).place(x=0,y=150)

        self.id=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.id).place(x=30,y=30)
        self.fecha=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.fecha).place(x=52,y=60)
        self.tiempo_dias=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.tiempo_dias).place(x=42,y=90)
        self.id_cliente=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.id_cliente).place(x=92,y=120)
        self.importe=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.importe).place(x=62,y=150)
        
        Button(self.ventanaIngresar,text="Guardar",font=("Cambria",11),
                   width=15,command=self.BD).place(x=420,y=5)
        
        Button(self.ventanaIngresar,text="Kruskal",font=("Cambria",11),
                   width=15,command=self.grafo).place(x=420,y=365)
                   
        Button(self.ventanaIngresar,text="Mostrar",font=("Cambria",11),
                     width=15,command=self.Mostrar).place(x=0,y=365)
                     
        Button(self.ventanaIngresar,text="Ordenar",font=("Cambria",11),
                     width=15,command=self.Ordenamiento).place(x=220,y=365)
        
        
        self.ventanaIngresar.mainloop() 
    def Ordenamiento(self):
        comando="SELECT importe FROM inversion;"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        rows= conectar.cursor.fetchall()
        tiempo_inicial = time()
        ordenar=MergeSort.merge_sort(rows)
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        print(ordenar)
        #print("El tiempo de ejecucion fue de:",tiempo_ejecucion)
    def BD(self):
        conectar=Base_de_datos.BaseDeDatos()
        comando="INSERT INTO inversion(id,fecha,tiempo_dias,id_cliente,importe) VALUES('"+self.id.get()+"','"+self.fecha.get()+"','"+self.tiempo_dias.get()+"','"+self.id_cliente.get()+"','"+self.importe.get()+"')"
        print(comando)
        conectar.cursor.execute(comando)
    def Mostrar(self):
        comando="SELECT * FROM inversion;"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        Scroll=Scrollbar(self.ventanaIngresar, orient=VERTICAL)
        self.listbox=Listbox(self.ventanaIngresar, font=("Cambria",9), borderwidth=0, yscrollcommand=Scroll.set,height=11,relief="sunken",width=70)
        self.listbox.place(x=5, y=180)
        Scroll.config(command=self.listbox.yview)
        Scroll.pack(side=RIGHT, fill=Y)
        for dato1, dato2 in enumerate(conectar.cursor.fetchall()):
            self.listbox.insert(0, "Id: {}".format(dato2[0]))
            self.listbox.insert(1, "Fecha: {}".format(dato2[1]))
            self.listbox.insert(2, "Dias: {}".format(dato2[2]))
            self.listbox.insert(3, "Id del cliente: {}".format(dato2[3]))
            self.listbox.insert(4, "Importe: {}".format(dato2[4]))
            self.listbox.insert(5, " ")
    def grafo(self):
        self.palabra=None
        self.palabra2=None
        self.ventanaBusqueda=Toplevel()
        self.ventanaBusqueda.geometry("265x298")
        self.ventanaBusqueda.title("Grafo")
        Label(self.ventanaBusqueda, text="fecha origen mm/dd/aa",font=("Calibri Light",14)).place(x=5,y=0)
        self.palabra=StringVar()
        Entry(self.ventanaBusqueda, textvariable=self.palabra).place(x=70,y=30)
        Label(self.ventanaBusqueda, text="fecha final mm/dd/aa",font=("Calibri Light",14)).place(x=5,y=60)
        self.palabra2=StringVar()
        Entry(self.ventanaBusqueda, textvariable=self.palabra2).place(x=70,y=90)
        Button(self.ventanaBusqueda,text="Buscar",font=("Cambria",11),
                   width=10,command=self.funcionGrafo).place(x=90,y=120)
    def funcionGrafo(self):
        #01/01/2018 - 01/30/2018
        contador = 0
        comando="SELECT * FROM inversion where fecha >='"+self.palabra.get()+"'AND fecha <'"+self.palabra2.get()+"';"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        self.listbox2=Listbox(self.ventanaBusqueda, font=("Cambria",11), borderwidth=0, height=7,relief="sunken",width=30)
        self.listbox2.place(x=7, y=155)
        g=Grafo
        arista = []
        tiempo_inicial = time()
        for dato1, self.dato2 in enumerate(conectar.cursor.fetchall()):
            arista.append(g.Kruskal(self.dato2[1],self.dato2[3],self.dato2[4]))
            contador+=1
        result = g.kruskal(arista) 
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        for self.i in result:
            self.listbox2.insert(0, "Id del cliente: {}".format(self.i.dato2))
            self.listbox2.insert(1, "Importe: {}".format(self.i.peso))  
            self.listbox2.insert(2, " ")
        print("El tiempo de ejecucion fue de:",tiempo_ejecucion)
        print(contador)
