# 4 . Nested if
a = float(input("Input base number of triangle : "))
t = float(input("Input Height number of triangle : "))
#Kamus
areaTriangle = a * t / 2
#Logaritma
if areaTriangle > 0 :
    if areaTriangle != 0 :
        print(areaTriangle)
    else :
        print("Base and height cannot be 0")
else :
    print("Base and height cannot be minus")