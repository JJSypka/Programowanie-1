def f2(a1,a2):
    ilosc_gwiazdek = 0
    for liczba in a1:
        if liczba in a2:
            ilosc_gwiazdek += 1
        else:
            continue
    x = ilosc_gwiazdek * "*"
    return x

print (f2([10,20,38],[14,9,10,31,20]))
        