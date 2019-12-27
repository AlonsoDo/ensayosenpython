#!/usr/bin/env python
print("Comprobador de anos bisiestos")
fecha = int(input("Escriba un ano y le dire si es bisiesto: "))

if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
    print("El ano", fecha, "es un ano bisiesto.")
else:
    print("El ano", fecha, "no es un ano bisiesto.")
