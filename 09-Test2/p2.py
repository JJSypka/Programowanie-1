def f(human_age):
    if human_age > 2:
        age = 20 + (human_age -2) *4
    elif human_age ==2:
        age = 20
    elif human_age == 1:
        age = 10
    return age


print(f(15))
print(f(2))
