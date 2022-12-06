lista = [2,3,2,5,8,1,9,8]
lista1=[]

n=0
for numer in lista:
    lista.pop(n)
    if numer in lista:
        n +=1
        continue
    
    else:
        lista1.append(numer)
        n +=1
print(lista1)