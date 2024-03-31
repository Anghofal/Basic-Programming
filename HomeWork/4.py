#Kasus 1
n = int(input()) 
if n > 12 :
    print("Bilangan lebih dari 12")

#Kasus 2
n = int(input())
print(n)

#Kasus 3
x = str(input())
print(x)

#Kasus 4
p = float(input())
l = float(input())
a = p * l # a : luas persegi panjang
print(a)
if p == l :
    print("Ini persegi")

#Kasus 5
p = float(input())
l = float(input())
j = str(input())
a = p * l
b = p * l / 2
if j == "setuju" :
    print(a)
    print(a)
if j == "tidak setuju" :
    print(a)
    print(b)
