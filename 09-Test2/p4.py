# jak iterowac po listach w dict
def f(dictionary,x,y):
    sum =0
    for values in dictionary:
        for i in dictionary[values]:
            if i >=x and i <= y:
                sum += i
                print (sum)
    return sum
#co potreba do csv    
import csv
reader = csv.reader("nazwa_pliku",delimiter=',')
for line in reader:
    print(line)

#co do json
import json
with open(„nazwa”,”mode”) as file:
reader = json.load(file)
#lista, ktora jako elementy ma liste
def f(array2D):
    sum=[]
    for x in range(len(array2D[0])):
        suma=0
        for y in range(len(array2D)):
            suma += array2D[y][x]
        sum.append(suma)
    return sum
