#!/usr/bin/env python
anchura = int(input("Anchura del rectangulo: "))
altura = int(input("Altura del rectangulo: "))

for i in range(altura):
    for j in range(anchura):
        print("* ", end="")
    print()

