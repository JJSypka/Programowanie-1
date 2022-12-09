a = 0
x = int(input("Wproadz liczbe: "))
while a<x:
    if a == 0 or a == 1 or a==2 or a ==5:
        print(a, end=" ")
        a += 1
    elif a % 2== 0 or a % 3 == 0 or a % 5 == 0 or a % 7==0:
        a +=1
        continue
    else:
        print (a, end=" ")
        a +=1
