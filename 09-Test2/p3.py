def f(array2D):
    sum=[]
    for x in range(len(array2D[0])):
        suma=0
        for y in range(len(array2D)):
            suma += array2D[y][x]
        sum.append(suma)
    return sum


print(f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]))