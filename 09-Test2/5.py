import re 
def f5(c, n):
    
    hand = open('/Users/jj/Desktop/Studia/Semestr 3/Programowanie 1/Programowanie-1/09-Test2/beautybeast.txt') 
    for line in hand:
        line = line.readlines(n)
        if re.search(rf'[{c}]', line):
            return True

print(f5("s",3))