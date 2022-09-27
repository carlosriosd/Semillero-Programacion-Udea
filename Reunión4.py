#Este algoritmo de ordenamiento es el mismo de la Reunión 2 Ejercicio 7

def bubblesort(array):
    #print(array)
    for j in range(len(array)):            
        for i in range(len(array)-1-j):
            if array[i] > array[i+1]:
                aux = array[i]
                array[i] = array[i+1]
                array[i+1] = aux
    return array

def mergesort(array):

  if len(array) <= 1:
    return array
    
  if len(array) == 2:
    if array[0] <= array[1]:
      temp = [array[0],array[1]]
    else:
      temp = [array[1],array[0]]
    return temp
    
  else:
    lista = []
    left = mergesort(array[:int(len(array)/2)])
    right = mergesort(array[int(len(array)/2):])
    cont = 0
    last_L = 0
    last_R = 0
    for i in range(len(left)):
      last_L = i
      for j in range(cont, len(right)):
        last_R = j
        if right[j] <= left[i]:
          lista.append(right[j])
        else:
          lista.append(left[i])
          break
        cont += 1
        
    if lista[-1] < left[last_L]:
      for i in left[last_L:]:
        lista.append(i)
        
    if lista[-1] < right[last_R]:
      for i in right[last_R:]:
        lista.append(i)
        
    return lista


lista = [27,45,11,-3,0,-50,21,3,7]

print(mergesort(lista))


import random, timeit
import matplotlib.pyplot as plt

time = []
time2 = []
it = []


for i in range(1000):
  it.append(i)
  randomlist = random.sample(range(-1000, 1000), i)
  start = timeit.default_timer()
  mergesort(randomlist)
  stop = timeit.default_timer()
  time.append(stop-start)
  
for i in range(1000):
  randomlist = random.sample(range(-1000, 1000), i)
  start = timeit.default_timer()
  bubblesort(randomlist)
  stop = timeit.default_timer()
  time2.append(stop-start)
  
plt.plot(it,time, label = "Merge Sort")
plt.plot(it,time2, label = "Bubble Sort")
plt.legend()
plt.show
