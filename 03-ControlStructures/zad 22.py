for i in range (1,31):
    if i%3 == 0 and i%5==0:
        c= "Bingo"
        print(c, end=' ')
    elif i% 5 ==0:
        b= "FIVE"
        print(b, end=" ")
    elif i% 3 == 0:
        a = "Three"
        print (a, end=" ")
    else:
        print (i, end=" ")