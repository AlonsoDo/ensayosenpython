#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el m?todo constructor __init__(): Uno de
# ellos es el bot?n 'Info'  que cuando sea presionado llamar? 
# al m?todo 'verinfo' para mostrar informaci?n en el otro 
# widget, una caja de texto: un evento ejecuta una acci?n: 

class Aplicacion():
    def __init__(self):
        
        # En el ejemplo se utiliza el prefijo 'self' para
        # declarar algunas variables asociadas al objeto 
        # ('mi_app')  de la clase 'Aplicacion'. Su uso es 
        # imprescindible para que se pueda acceder a sus
        # valores desde otros m?todos:
        
        self.raiz = Tk()
        self.raiz.geometry('300x200')
        
        # Impide que los bordes puedan desplazarse para
        # ampliar o reducir el tama?o de la ventana 'self.raiz':
        
        self.raiz.resizable(width=False,height=False)
        self.raiz.title('Ver info')
        
        # Define el widget Text 'self.tinfo ' en el que se
        # pueden introducir varias l?neas de texto:
        
        self.tinfo = Text(self.raiz, width=40, height=10)
        
        # Sit?a la caja de texto 'self.tinfo' en la parte
        # superior de la ventana 'self.raiz':
        
        self.tinfo.pack(side=TOP)
        
        # Define el widget Button 'self.binfo' que llamar? 
        # al metodo 'self.verinfo' cuando sea presionado
        
        self.binfo = ttk.Button(self.raiz, text='Info', 
                                command=self.verinfo)
        
        # Coloca el bot?n 'self.binfo' debajo y a la izquierda
        # del widget anterior
                                
        self.binfo.pack(side=LEFT)
        
        # Define el bot?n 'self.bsalir'. En este caso
        # cuando sea presionado, el m?todo destruir? o
        # terminar? la aplicaci?n-ventana 'self.ra?z' con 
        # 'self.raiz.destroy'
        
        self.bsalir = ttk.Button(self.raiz, text='Salir', 
                                 command=self.raiz.destroy)
                                 
        # Coloca el bot?n 'self.bsalir' a la derecha del 
        # objeto anterior.
                                 
        self.bsalir.pack(side=RIGHT)
        
        # El foco de la aplicaci?n se sit?a en el bot?n
        # 'self.binfo' resaltando su borde. Si se presiona
        # la barra espaciadora el bot?n que tiene el foco
        # ser? pulsado. El foco puede cambiar de un widget
        # a otro con la tecla tabulador [tab]
        
        self.binfo.focus_set()
        self.raiz.mainloop()
    
    def verinfo(self):
        
        # Borra el contenido que tenga en un momento dado
        # la caja de texto
        
        self.tinfo.delete("1.0", END)
        
        # Obtiene informaci?n de la ventana 'self.raiz':
        
        info1 = self.raiz.winfo_class()
        info2 = self.raiz.winfo_geometry()
        info3 = str(self.raiz.winfo_width())
        info4 = str(self.raiz.winfo_height())
        info5 = str(self.raiz.winfo_rootx())
        info6 = str(self.raiz.winfo_rooty())
        info7 = str(self.raiz.winfo_id())
        info8 = self.raiz.winfo_name()
        info9 = self.raiz.winfo_manager()
        
        # Construye una cadena de texto con toda la
        # informaci?n obtenida:
        
        texto_info = "Clase de 'raiz': " + info1 + "\n"
        texto_info += "Resolucion y posicion: " + info2 + "\n"
        texto_info += "Anchura ventana: " + info3 + "\n"
        texto_info += "Altura ventana: " + info4 + "\n"
        texto_info += "Pos. Ventana X: " + info5 + "\n"
        texto_info += "Pos. Ventana Y: " + info6 + "\n"
        texto_info += "Id. de 'raiz': " + info7 + "\n"
        texto_info += "Nombre objeto: " + info8 + "\n" 
        texto_info += "Gestor ventanas: " + info9 + "\n"
        
        # Inserta la informaci?n en la caja de texto:
        
        self.tinfo.insert("1.0", texto_info)

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()

