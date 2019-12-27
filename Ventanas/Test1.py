#!/usr/bin/env python
## -*- coding: utf-8 -*-

# Las dos l?neas siguientes son necesaias para hacer 
# compatible el interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las mas recientes. 

from tkinter import *    # Carga modulo tk (widgets estandar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

# Define la ventana principal de la aplicacion

raiz = Tk()

# Define las dimensiones de la ventana, que se ubicara en 
# el centro de la pantalla. Si se omite esta linea la
# ventana se adaptara a los widgets que se coloquen en
# ella. 

raiz.geometry('300x200') # anchura x altura

# Asigna un color de fondo a la ventana. Si se omite
# esta linea el fondo sera gris

raiz.configure(bg = 'beige')

# Asigna un titulo a la ventana

raiz.title('Aplicacion')

# Define un boton en la parte inferior de la ventana
# que cuando sea presionado hara que termine el programa.
# El primer parametro indica el nombre de la ventana 'raiz'
# donde se ubicara el boton

ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)

# Despues de definir la ventana principal y un widget boton
# la siguiente l?nea hara que cuando se ejecute el programa
# construya y muestre la ventana, quedando a la espera de 
# que alguna persona interactue con ella.

# Si la persona presiona sobre el boton Cerrar 'X', o bien,
# sobre el boton 'Salir' el programa llegara a su fin.

raiz.mainloop()
