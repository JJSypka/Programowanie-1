def f4(d,n):
    sum = 0
    for keys in d:
        if keys["age"] > n:
            sum += 1
    return sum

print(f4([{"name":"Peter", "age":30}, {"name":"Chuj", "age":25}], 20))