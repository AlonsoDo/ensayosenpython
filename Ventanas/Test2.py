#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

# Crea una clase Python para definir el interfaz de usuario de
# la aplicaci?n. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutar? autom?ticamente el m?todo __init__() qu? 
# construye y muestra la ventana con todos sus widgets: 

class Aplicacion():
    def __init__(self):
        raiz = Tk()
        raiz.geometry('300x200')
        raiz.configure(bg = 'beige')
        raiz.title('Aplicacion')
        ttk.Button(raiz, text='Salir', 
                   command=raiz.destroy).pack(side=BOTTOM)
        raiz.mainloop()

# Define la funci?n main() que es en realidad la que indica 
# el comienzo del programa. Dentro de ella se crea el objeto 
# aplicaci?n 'mi_app' basado en la clase 'Aplicaci?n':

def main():
    mi_app = Aplicacion()
    return 0

# Mediante el atributo __name__ tenemos acceso al nombre de un
# un m?dulo. Python utiliza este atributo cuando se ejecuta
# un programa para conocer si el m?dulo es ejecutado de forma
# independiente (en ese caso __name__ = '__main__') o es 
# importado:

if __name__ == '__main__':
    main()
