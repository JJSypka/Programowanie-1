def compare(array1,array2):
    if len(array1) == len(array2):
        n=0
        for i in array1:
            if array1[n]== array2[n] and n <= len(array1):
                n +=1
            else:
                return False
        
        return True
    else:
        return False

print(compare([True,False] ,[True,False,True]))