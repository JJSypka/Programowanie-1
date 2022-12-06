x = int(input("Podaj pierwsza wspolrzedna:"))
y= int(input("Podaj druga wspolrzedna"))

if x> 0 and y>0:
    print(f"Point p({x},{y}) is in the first quadrant of the coordinate system")
elif x<0 and y >0:
    print(f"Point p({x},{y}) is in the second quadrant of the coordinate system")
elif x<0 and y<0:
    print(f"Point p({x},{y}) is in the third quadrant of the coordinate system")
elif x> 0 and y <0:
    print(f"Point p({x},{y}) is in the fourth quadrant of the coordinate system")
