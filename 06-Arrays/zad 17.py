lista1 =[4,36,12,28,9,44,5]
lista2= [5,1,36]
lista3=[]
for numer in lista1:
    if numer  in lista2:
        continue
    else:
        lista3.append(numer)

print (lista3)
