from tkinter import *
import psycopg2
import sys
import pprint
import Base_de_datos
import MergeSort

class Pago_interes:
    def __init__(self,id=None,idinversion=None,fecha=None,importe=None):
            self.id=id
            self.idinversion = idinversion
            self.fecha = fecha
            self.importe = importe
    def ingresar(self):
        self.ventanaIngresar=Toplevel()
        self.ventanaIngresar.geometry("570x400")
        self.ventanaIngresar.title("Pago de intereses")
        img = PhotoImage(file="C:/Users/checo/Desktop/41-INVERSION-MEDIOS-DIGITALES.png")
        imagen= Label(self.ventanaIngresar, image=img)
        imagen.pack()
        Label(self.ventanaIngresar, text="Pago de intereses",font=("Cambria",14)).place(x=5,y=0)
        Label(self.ventanaIngresar, text="Id: ",font=("Cambria",11)).place(x=0,y=30)
        Label(self.ventanaIngresar, text="Id de inversion: ",font=("Cambria",11)).place(x=0,y=60)
        Label(self.ventanaIngresar, text="Fecha: ",font=("Cambria",11)).place(x=0,y=90)
        Label(self.ventanaIngresar, text="Importe: ",font=("Cambria",11)).place(x=0,y=120)

        self.id=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.id).place(x=30,y=30)
        self.idinversion=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.idinversion).place(x=115,y=60)
        self.fecha=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.fecha).place(x=55,y=90)
        self.importe=StringVar()
        Entry(self.ventanaIngresar, textvariable=self.importe).place(x=85,y=120)
        
        Button(self.ventanaIngresar,text="Guardar",font=("Cambria",11),
                   width=15,command=self.BD).place(x=420,y=5)
        
        #Button(self.ventanaIngresar,text="Modificar",font=("Cambria",11),
        #           width=15).place(x=420,y=365)
                   
        Button(self.ventanaIngresar,text="Mostrar",font=("Cambria",11),
                     width=15,command=self.Mostrar).place(x=0,y=365)
                     
        Button(self.ventanaIngresar,text="Ordenar",font=("Cambria",11),
                     width=15,command=self.Ordenamiento).place(x=220,y=365)
        
        self.ventanaIngresar.mainloop()   
    def Ordenamiento(self):
        comando="SELECT importe FROM pago_interes;"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        rows= conectar.cursor.fetchall()
        ordenar=MergeSort.merge_sort(rows)
        print(ordenar)
    def BD(self):
        conectar=Base_de_datos.BaseDeDatos()
        comando="INSERT INTO pago_interes(id,id_inversion,fecha,importe) VALUES('"+self.id.get()+"','"+self.idinversion.get()+"','"+self.fecha.get()+"','"+self.importe.get()+"')"
        print(comando)
        conectar.cursor.execute(comando)
    def Mostrar(self):
        comando="SELECT * FROM pago_interes;"
        conectar=Base_de_datos.BaseDeDatos()
        conectar.cursor.execute(comando)
        Scroll=Scrollbar(self.ventanaIngresar, orient=VERTICAL)
        self.listbox=Listbox(self.ventanaIngresar, font=("Cambria",9), borderwidth=0, yscrollcommand=Scroll.set,height=11,relief="sunken",width=70)
        self.listbox.place(x=5, y=180)
        Scroll.config(command=self.listbox.yview)
        Scroll.pack(side=RIGHT, fill=Y)
        self.listbox.insert(END, "Datos" )
        for dato1, dato2 in enumerate(conectar.cursor.fetchall()):
            self.listbox.insert(0, "Id: {}".format(dato2[0]))
            self.listbox.insert(1, "Id de inversion: {}".format(dato2[1]))
            self.listbox.insert(2, "Fecha: {}".format(dato2[2]))
            self.listbox.insert(3, "Importe: {}".format(dato2[3]))
            self.listbox.insert(4, " ")
