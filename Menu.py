#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
import sys
import random 
import TipoInversion
import Cliente
import Inversion
import PagoIntereses

if __name__=='__main__':
    ventanaPrincipal = Tk()
    ventanaPrincipal.geometry("350x300")
    ventanaPrincipal.title("Prestamos")
    barraMenu=Menu (ventanaPrincipal)
    menuArchivo=Menu(barraMenu)

    tipo_inversion=TipoInversion.Tipo_inversion()
    cliente=Cliente.Cliente()
    inversion=Inversion.Inversion()
    pago_interes=PagoIntereses.Pago_interes()
    Label(text="PROGRAMA DE INVERSIONES", font=("Agency FB",14)).pack()
    img = PhotoImage(file="C:/Users/checo/Desktop/41-INVERSION-MEDIOS-DIGITALES.png")
    imagen= Label(image=img)
    imagen.pack()
    Button(ventanaPrincipal,text="Tipo de inversion",command=tipo_inversion.ingresar,font=("Agency FB",14),
                   width=15).place(x=120,y=30)
    Button(ventanaPrincipal,text="Clientes",command=cliente.ingresar,font=("Agency FB",14),
                  width=15).place(x=120,y=90)
    Button(ventanaPrincipal,text="Inversion",command=inversion.ingresar,font=("Agency FB",14),
                    width=15).place(x=120,y=150)
    Button(ventanaPrincipal,text="Pago de intereses",command=pago_interes.ingresar,font=("Agency FB",14),
                    width=15).place(x=120,y=210)
                    
    menuArchivo.add_command(label="Tipo de inversion", command=tipo_inversion.ingresar)
    menuArchivo.add_command(label="Clientes",command=cliente.ingresar)
    menuArchivo.add_command(label="Inversion",command=inversion.ingresar)
    menuArchivo.add_command(label="Pago de intereses",command=pago_interes.ingresar)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Salir",command=ventanaPrincipal.destroy)

    barraMenu.add_cascade(label="Opciones",menu=menuArchivo)
    ventanaPrincipal.config(menu=barraMenu)

    ventanaPrincipal.mainloop()

"""
def modificar():
    ventanaModificar=Toplevel(ventanaPrincipal)
    ventanaModificar.geometry("350x300")
    ventanaModificar.title("Modificar")
    
    
    ventanaModificar.mainloop() 
""" 
    
