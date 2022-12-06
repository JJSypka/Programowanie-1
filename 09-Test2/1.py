def f1(a,c):
    sum=0
    for slowo in a:
        for litera in slowo:
            if litera == c:
                sum +=1
            else:
                continue
    return sum


print(f1(["sun"," moon","sand"], "n"))