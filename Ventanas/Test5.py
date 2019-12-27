#!/usr/bin/env python
from tkinter import *
from tkinter import ttk, font
import getpass

# Gestor de geometr?a (grid). Ventana no dimensionable

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")
        
        # Establece que no se pueda modificar el tama?o de la
        # ventana. El m?todo resizable(0,0) es la forma abreviada 
        # de resizable(width=False,height=False).
        
        self.raiz.resizable(0,0)
        fuente = font.Font(weight='bold')
        
        # Define un widget de tipo 'Frame' (marco) que ser? el
        # contenedor del resto de widgets. El marco se situar? 
        # en la ventana 'self.raiz' ocupando toda su extensi?n.
        # El marco se define con un borde de 2 p?xeles y la
        # opci?n 'relief' con el valor 'raised' (elevado) a?ade
        # un efecto 3D a su borde. 
        # La opci?n 'relief' permite los siguientes valores:
        # FLAT (llano), RAISED (elevado), SUNKEN (hundido),
        # GROOVE (hendidura) y RIDGE (borde elevado).
        # La opci?n 'padding' a?ade espacio extra interior para
        # que los widgets no queden pegados al borde del marco.
          
        self.marco = ttk.Frame(self.raiz, borderwidth=2,
                               relief="raised", padding=(10,10))
                               
        # Define el resto de widgets pero en este caso el primer 
        # par?metro indica que se situar?n en el widget del 
        # marco anterior 'self.marco'.
                               
        self.etiq1 = ttk.Label(self.marco, text="Usuario:", 
                               font=fuente, padding=(5,5))
        self.etiq2 = ttk.Label(self.marco, text="Contrasena:",
                               font=fuente, padding=(5,5))
                               
        # Define variables para las opciones 'textvariable' de
        # cada caja de entrada 'ttk.Entry()'.
        
        self.usuario = StringVar()
        self.clave = StringVar()
        self.usuario.set(getpass.getuser())        
        self.ctext1 = ttk.Entry(self.marco, textvariable=self.usuario, 
                                width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable=self.clave, 
                                show="*", 
                                width=30)
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marco, text="Aceptar", 
                                 padding=(5,5), command=self.aceptar)
        self.boton2 = ttk.Button(self.marco, text="Cancelar", 
                                 padding=(5,5), command=quit)
        
        # Define la ubicaci?n de cada widget en el grid.
        # En este ejemplo en realidad hay dos grid (cuadr?culas):
        # Una cuadr?cula de 1fx1c que se encuentra en la ventana 
        # que ocupar? el Frame; y otra en el Frame de 5fx3c para
        # el resto de controles.
        # La primera fila y primera columna ser?n la n?mero 0.
        # La opci?n 'column' indica el n?mero de columna y la
        # opci?n 'row' indica el n?mero de fila donde hay que 
        # colocar un widget. 
        # La opci?n 'columnspan' indica al gestor que el 
        # widget ocupar? en total un n?mero determinado de
        # columnas. Las cajas para entradas 'self.ctext1' y
        # 'self.ctext2' ocupar?n dos columnas y la barra
        # de separaci?n 'self.separ1' tres.
        
        self.marco.grid(column=0, row=0)
        self.etiq1.grid(column=0, row=0)
        self.ctext1.grid(column=1, row=0, columnspan=2)
        self.etiq2.grid(column=0, row=1)
        self.ctext2.grid(column=1, row=1, columnspan=2)
        self.separ1.grid(column=0, row=3, columnspan=3)
        self.boton1.grid(column=1, row=4)
        self.boton2.grid(column=2, row=4)

        # Establece el foco en la caja de entrada de la
        # contrase?a.

        self.ctext2.focus_set()
        self.raiz.mainloop()
    
    def aceptar(self):
        if self.clave.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario:   ", self.ctext1.get())
            print("Contrasena:", self.ctext2.get())
        else:
            print("Acceso denegado")
            self.clave.set("")
            self.ctext2.focus_set()

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
