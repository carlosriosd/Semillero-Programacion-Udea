#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:20:10 2022

@author: carlos
"""

def ejercicio1():
  """"Write a Python program calculate the product, multiplying all the numbers of a given tuple"""
  tupla = (3,5,8,-4,23,41,26)
  multiplicacion = 1
  for i in tupla:
    multiplicacion *= i  
  print(multiplicacion)

def ejercicio2():
  """"Write a Python program to calculate the average value of the numbers in a given tuple of tuples."""
  #El promedio de los promedios no es el promedio de todos los números
  tupla = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4),(2,3),(5,8,9))
  promedio = []
  for i in tupla:
    promedio.append(sum(i)/len(i))
  print(sum(promedio)/len(promedio))
  suma = 0
  contador = 0
  for i in tupla:
    for j in i:
      suma += j
      contador += 1
  print(suma/contador)

def ejercicio3():
  """"Write a Python program to check if a specified element presents in a tuple of tuples."""
  tupla = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
  busqueda = str(input("Término a buscar: "))
  for i in tupla:
    if busqueda in i:
      print("Está en la tupla", i)

def ejercicio4():
  """"Write a Python program to convert a given list of tuples to a list of lists."""
  tupla = [(1, 2), (2, 3), (3, 4)]
  
  #Forma 1
  lista = []
  for i in tupla:
    arreglo = []
    for j in i:
      arreglo.append(j)
    lista.append(arreglo)
  print(lista)
  
  #Forma 2
  for i in range(len(tupla)):
    tupla[i] = list(tupla[i])
  print(tupla)



#Busar el máximo de una lista
def ejercicio5(a, b, c):
  print(max((a,b,c)))

def ejercicio6(array):
  maximo = array[0]
  for i in array[1::]:
    if i > maximo:
      maximo = i
    print(maximo)

#Ordenar listas
def ejercicio7(array):
  print(array)
  for j in range(len(array)):            
    for i in range(len(array)-1-j):
      if array[i] > array[i+1]:
        aux = array[i]
        array[i] = array[i+1]
        array[i+1] = aux

  print(array)
if __name__ == "__main__":
  ejercicio1()
  ejercicio2()
  ejercicio3()
  ejercicio4()
  ejercicio5(25.34,13.26,21.58) 
  ejercicio6((35,24,86,101,92,46,123,112,3,5,99,110,123,0,-7,-123))  
  ejercicio7([35,24,86,101,92,46,123,112,3,5,99,110,123,0,-7,-123])