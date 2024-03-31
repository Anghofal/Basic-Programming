x = int(input("Number 1 : "))
y = int(input("Number 2 : "))
z = int(input("Number 3 : "))

if (x > y > z) :
    print("Number 1 is Biggest")
elif (x < y > z) :
    print("Number 2 is Biggest") 
else:
    print("Number 3 is Biggest")

if (x < y < z) :
    print("Number 1 is Smallest")
elif (x > y < z) :
    print("Number 2 is Smallest")
else:
    print("Number 3 is Smallest")
