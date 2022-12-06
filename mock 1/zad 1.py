def f1(card_number):
    card_number= str(card_number)
    x=list(map(str,card_number))
    x[2]="*"
    x[3]="*"
    x[4]="*"
    x[5]="*"
    x[6]="*"
    x[7]="*"
    x[8]="*"
    x[9]="*"
    x[10]="*"
    x[11]="*"
    numerek=""
    for i in x:
        numerek+=str(i)
    
    return numerek



def f2(binary_number):
    for i in binary_number:
        if i!=0 or i!=1:    
            return False
    return True

print(f2("1010101001"))
print(f2("1070101"))




