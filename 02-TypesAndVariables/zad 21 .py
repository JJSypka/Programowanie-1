import random

computer_dice = random.randrange(1 , 6)
user_dice = int(input("Wprowadz liczbe oczek:"))
if computer_dice == user_dice:
    print (True)
else:
    print(False)
