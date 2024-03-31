p = int(input("Input the length : "))
l = int(input("Input the width : "))
r = float(input("Input circle radius : "))

squareArea = p * p 
rectangleArea = p * l
pi = 3.14
circleArea = pi * r * r


if (p != 0):
    print(squareArea, "This is Square Area")
if (p,l) != 0:
    print(rectangleArea, "This is Rectangle Area")
if (r != 0):
    print(circleArea, "This is Circle Area")
    

    
    

