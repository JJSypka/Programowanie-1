def sum(array):
    suma=0
    for number in array:
        suma +=number
    return suma

def array2str(array):
    string= ""
    for number in array:
        string += str(number) +" "
    return string

ar=array2str([4,3,7,1,3])
xd=sum([4,3,7,1,3])
print(f"array: {ar}")
print(f"Sum of values: {xd}" )