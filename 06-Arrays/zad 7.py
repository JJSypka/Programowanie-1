lista=[1,2,3,4]
sumOfOdd=0
sumOfEven=0
for numer in lista:
    if numer % 2 ==0:
        sumOfEven+=1
    elif numer % 2 !=0:
        sumOfOdd+=1

print(f"Ilość parzystaych: {sumOfEven}\nIlosc nieparzystych: {sumOfOdd}")