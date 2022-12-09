
for attempt in range (1,4):
    pin= input("Podaj kod PIN:")
    if pin == "0805" :
        print ("Correct")
        break
    if attempt == 3:
        print( "incorrect,Sorry, your payment card has been blocked. ")
    else:
        print("Incorrect")
    