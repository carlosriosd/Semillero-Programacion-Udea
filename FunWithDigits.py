import itertools

def concat(array):
  letters = ""
  for i in array:
    letters += str(i)
  return letters

def findall(array, string):
  pos_array = []
  for i in range(len(array)):
    if array[i] == str(string):
      pos_array.append(i)
  return pos_array
    
numbers = [1,2,3,4,5,6,7,8,9]
places = [1,2,3,4,5,6,7,8]
Places = []

for i in range(1,len(places)+1):
  for j in list(itertools.combinations(places,i)):
    Places.append(j)

for i in Places:
  placement_array = numbers.copy()
  cont = 0
  
  for j in i:
    placement_array.insert(j+cont,"+")
    cont += 1
  value = eval(concat(placement_array))
  
  if value == 100:
    print("Secuencia encontrada: ", placement_array)
    
  else:
    plus_places=findall(concat(placement_array),"+")
    minus_places = []
    
    for j in range(1,len(plus_places)+1): 
      for k in list(itertools.combinations(plus_places,j)):
        minus_places.append(k)
        
    for j in minus_places:
      placement_minus_array = placement_array.copy()
      cont = 0
      
      for k in j:
        placement_minus_array.insert(k+cont, "-")
        cont += 1
        
      value = eval(concat(placement_minus_array))
      
      if value == 100:
        print("Secuencia encontrada: ", concat(placement_minus_array))
