#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass

# Gestor de geometr?a (pack)

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")
        
        # Cambia el formato de la fuente actual a negrita para
        # resaltar las dos etiquetas que acompa?an a las cajas
        # de entrada. (Para este cambio se ha importado el  
        # m?dulo 'font' al comienzo del programa):
        
        fuente = font.Font(weight='bold')
        
        # Define las etiquetas que acompa?an a las cajas de
        # entrada y asigna el formato de fuente anterior: 
                               
        self.etiq1 = ttk.Label(self.raiz, text="Usuario:", 
                               font=fuente)
        self.etiq2 = ttk.Label(self.raiz, text="Contrasena:", 
                               font=fuente)
        
        # Declara dos variables de tipo cadena para contener
        # el usuario y la contrase?a: 
        
        self.usuario = StringVar()
        self.clave = StringVar()
        
        # Realiza una lectura del nombre de usuario que 
        # inici? sesi?n en el sistema y lo asigna a la
        # variable 'self.usuario' (Para capturar esta
        # informaci?n se ha importando el m?dulo getpass
        # al comienzo del programa):
        
        self.usuario.set(getpass.getuser())
        
        # Define dos cajas de entrada que aceptar?n cadenas
        # de una longitud m?xima de 30 caracteres.
        # A la primera de ellas 'self.ctext1' que contendr?
        # el nombre del usuario, se le asigna la variable
        # 'self.usuario' a la opci?n 'textvariable'. Cualquier
        # valor que tome la variable durante la ejecuci?n del
        # programa quedar? reflejada en la caja de entrada.
        # En la segunda caja de entrada, la de la contrase?a,
        # se hace lo mismo. Adem?s, se establece la opci?n
        # 'show' con un "*" (asterisco) para ocultar la 
        # escritura de las contrase?as:
        
        self.ctext1 = ttk.Entry(self.raiz, 
                                textvariable=self.usuario, 
                                width=30)
        self.ctext2 = ttk.Entry(self.raiz, 
                                textvariable=self.clave, 
                                width=30, show="*")
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        
        # Se definen dos botones con dos m?todos: El bot?n
        # 'Aceptar' llamar? al m?todo 'self.aceptar' cuando
        # sea presionado para validar la contrase?a; y el bot?n
        # 'Cancelar' finalizar? la aplicaci?n si se llega a
        # presionar:
        
        self.boton1 = ttk.Button(self.raiz, text="Aceptar", 
                                 command=self.aceptar)
        self.boton2 = ttk.Button(self.raiz, text="Cancelar", 
                                 command=quit)
                                 
        # Se definen las posiciones de los widgets dentro de
        # la ventana. Todos los controles se van colocando 
        # hacia el lado de arriba, excepto, los dos ?ltimos, 
        # los botones, que se situar?n debajo del ?ltimo 'TOP':
        # el primer bot?n hacia el lado de la izquierda y el
        # segundo a su derecha.
        # Los valores posibles para la opci?n 'side' son: 
        # TOP (arriba), BOTTOM (abajo), LEFT (izquierda)
        # y RIGHT (derecha). Si se omite, el valor ser? TOP
        # La opci?n 'fill' se utiliza para indicar al gestor
        # c?mo expandir/reducir el widget si la ventana cambia
        # de tama?o. Tiene tres posibles valores: BOTH
        # (Horizontal y Verticalmente), X (Horizontalmente) e 
        # Y (Verticalmente). Funcionar? si el valor de la opci?n
        # 'expand' es True.
        # Por ?ltimo, las opciones 'padx' y 'pady' se utilizan
        # para a?adir espacio extra externo horizontal y/o 
        # vertical a los widgets para separarlos entre s? y de 
        # los bordes de la ventana. Hay otras equivalentes que
        # a?aden espacio extra interno: 'ip?dx' y 'ipady':
                                         
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, 
                         padx=5, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True, 
                         padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        
        # Cuando se inicia el programa se asigna el foco
        # a la caja de entrada de la contrase?a para que se
        # pueda empezar a escribir directamente:
                
        self.ctext2.focus_set()
        
        self.raiz.mainloop()
    
    # El m?todo 'aceptar' se emplea para validar la 
    # contrase?a introducida. Ser? llamado cuando se 
    # presione el bot?n 'Aceptar'. Si la contrase?a
    # coincide con la cadena 'tkinter' se imprimir?
    # el mensaje 'Acceso permitido' y los valores 
    # aceptados. En caso contrario, se mostrar? el
    # mensaje 'Acceso denegado' y el foco volver? al
    # mismo lugar.
    
    def aceptar(self):
        if self.clave.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario:   ", self.ctext1.get())
            print("Contrasena:", self.ctext2.get())
        else:
            print("Acceso denegado")
            
            # Se inicializa la variable 'self.clave' para
            # que el widget 'self.ctext2' quede limpio.
            # Por ?ltimo, se vuelve a asignar el foco
            # a este widget para poder escribir una nueva
            # contrase?a.
            
            self.clave.set("")
            self.ctext2.focus_set()

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()

