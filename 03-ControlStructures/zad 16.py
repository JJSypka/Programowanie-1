first_number = int(input("Wpisz pierwszą liczbe:"))
second_number= int (input("Wpisz drugą liczbe:"))
if first_number > second_number:
    print (f"Numbers in ascending order {second_number}, {first_number}")
elif first_number<second_number:
    print(f"Numbers in ascending order:{first_number},{second_number} ")
elif first_number == second_number:
    print ("The numbers are the same")