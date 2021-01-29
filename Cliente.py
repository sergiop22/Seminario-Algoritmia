from tkinter import *
import psycopg2
import sys
import pprint
import Base_de_datos
import MergeSort

class Cliente:
    def __init__(self,id=None,nombre=None):
            self.id=id
            self.nombre=nombre
    def ingresar(self):
        self.ventanaIngresar= Toplevel()
        self.ventanaIngresar.geometry("570x400")
        self.ventanaIngresar.title("Cliente")
        img = PhotoImage(file="C:/Users/checo/Desktop/41-INVERSION-MEDIOS-DIGITALES.png")
        imagen= Label(self.ventanaIngresar, image=img)
        imagen.pack()
        Label(self.ventanaIngresar, text="Cliente",font=("Cambria",14)).place(x=5,y=0)
        Label(self.ventanaIngresar, text="Id: ",font=("Cambria",11)).place(x=0,y=30)
        Label(self.ventanaIngresar, text="Nombre: ",font=("Cambria",11)).place(x=0,y=60)

        self.id=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.id).place(x=30,y=30)
        self.nombre=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.nombre).place(x=65,y=60) 
        
        Button(self.ventanaIngresar,text="Guardar",font=("Cambria",11),
                   width=15,command=self.BD).place(x=420,y=5)
        
        #Button(self.ventanaIngresar,text="Modificar",font=("Cambria",11),
        #           width=15).place(x=420,y=365)
                   
        Button(self.ventanaIngresar,text="Mostrar",font=("Cambria",11),
                     width=15,command=self.Mostrar).place(x=0,y=365)
                     
        Button(self.ventanaIngresar,text="Ordenar",font=("Cambria",11),
                     width=15, command=self.ordenamiento).place(x=220,y=365)
        
        self.ventanaIngresar.mainloop()
        
    def BD(self):
        conectar=Base_de_datos.BaseDeDatos()
        comando="INSERT INTO public.cliente(id, nombre) VALUES('"+self.id.get()+"','"+self.nombre.get()+"')"
        print(comando)
        conectar.cursor.execute(comando)
    def Mostrar(self):
        comando="SELECT * FROM cliente;"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        Scroll=Scrollbar(self.ventanaIngresar, orient=VERTICAL)
        self.listbox=Listbox(self.ventanaIngresar, font=("Cambria",9), borderwidth=0, yscrollcommand=Scroll.set,height=15,relief="sunken",width=60)
        self.listbox.place(x=5, y=90)
        Scroll.config(command=self.listbox.yview)
        Scroll.pack(side=RIGHT, fill=Y)
        for dato1, dato2 in enumerate(conectar.cursor.fetchall()):
            self.listbox.insert(0, "Id: {}".format(dato2[0]))
            self.listbox.insert(1, "Nombre: {}".format(dato2[1]))
            self.listbox.insert(2, " ")
    def ordenamiento(self):
        comando="SELECT id FROM cliente;"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        rows= conectar.cursor.fetchall()
        ordenar=MergeSort.merge_sort(rows)
        print(ordenar)

