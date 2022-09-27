#HackerRank Day 4

class Person:
  def __init__(self, age):
    if age >= 0:
      self.age = age
    else:
      self.age = 0
      print("Age is not valid, setting age to 0.")

  def yearPasses(self):
    self.age += 1
    #print(self.age)
    
  def amIOld(self):
    if self.age < 13:
      print("You are young.")
    elif self.age >= 13 and self.age < 18:
      print("You are a teenager.")
    else:
      print("You are old.")

#Test Cases
      
t = 4
for i in range(0, t):
    age = [-1,10,16,18][i]       
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

  
#Algoritmos de Ordenamiento

#Merge Sort

import math as m
import numpy as np

"""
np.random.seed(15)
lista = np.random.randint(100, size = 10)
print(lista)

def merge(arreglo):
  n = len(arreglo)

  aux = np.array_split(arreglo, 2)
  for i in aux:
    if len(i) == 1:
      return aux
    else:
      merge(i)
  

merge(lista)"""

#Insertion Sort
