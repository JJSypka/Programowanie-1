suma = 0
lista = []
while True:
    x = int(input("Wprowadz liczbe: "))
    if x == 0:
        break
    suma += x
    lista.append(x)
y = len(lista)
mean = suma/int(len(lista))
print(f"Result: Quantity ={y}, Sum = {suma}, Mean= {mean}")