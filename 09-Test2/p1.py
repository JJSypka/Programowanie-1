def f(player1,player2):
    sumOfplayer1=0
    sumOfplayer2=0
    for i in player1:
        if i == "A" or i == "K" or i=="Q" or i=="J" or i=="T":
            sumOfplayer1 +=10
        elif i=="9":
            sumOfplayer1+=9
        elif i=="8":
            sumOfplayer1+=8
        elif i=="7":
            sumOfplayer1+=7
        elif i=="6":
            sumOfplayer1+=6
        elif i=="5":
            sumOfplayer1+=5
        elif i=="4":
            sumOfplayer1+=4
        elif i=="3":
            sumOfplayer1+=3
        elif i=="2":
            sumOfplayer1+=2
    for i in player2:
        if i == "A" or i == "K" or i=="Q" or i=="J" or i=="T":
            sumOfplayer2 +=10
        elif i=="9":
            sumOfplayer2+=9
        elif i=="8":
            sumOfplayer2+=8
        elif i=="7":
            sumOfplayer2+=7
        elif i=="6":
            sumOfplayer2+=6
        elif i=="5":
            sumOfplayer2+=5
        elif i=="4":
            sumOfplayer2+=4
        elif i=="3":
            sumOfplayer2+=3
        elif i=="2":
            sumOfplayer2+=2
    if sumOfplayer2 > sumOfplayer1:
        return False
    elif sumOfplayer1> sumOfplayer2:
        return True
    elif sumOfplayer1 == sumOfplayer2:
        return False
print(f("AJ972","AQT72"))
print(f("9532","K8"))
print(f("987","AT4"))
