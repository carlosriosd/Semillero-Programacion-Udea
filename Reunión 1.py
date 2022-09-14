#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:21:35 2022

@author: carlos
"""

cadena = "Hola Mundo"

print(cadena[0]) #Imprimir primer caracter
print(cadena[4]) #Imprimir cualquier caracter
print(cadena[-1]) #Imprimir cualquier caracter

print(cadena[1:2:3]) #De la posición 1 a la posición 2 de 3 en 3 sin contar el límite superior

nueva_variable = cadena[0:4]+" grupo"
print(nueva_variable)

print(cadena.split())

import numpy as np
aurea = (1+np.sqrt(5))/2
pos = int(input("Posición: "))
lista = [0, 1]
start = 0
if pos > 1:
    for i in range(pos-2):
      lista.append(lista[-1]+lista[-2])
    print(lista[-1])
    print(lista)
else:
    print(lista[pos-1])
razon_aurea=[lista[2]/lista[1]]
contador = 3
while np.abs(razon_aurea[-1]-aurea)/aurea> 1e-32:
    try:
        razon_aurea.append(lista[contador]/lista[contador-1])
        contador += 1
    except:
        print("error")
        break
print(razon_aurea[-1])
print(contador)