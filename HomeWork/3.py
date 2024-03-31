#Kasus 1
a = 1
b = 4
print("Hasol a yamg pertama : " +str(a))
print("Hasol a yamg pertama : " +str(b))
b = a
a -= b
print("Hasol a yamg kedua : " +str(a))
print("Hasol a yamg kedua : " +str(b))
a = b + 1
b = a / b
print("Hasil a yang ketiga: " +str(a))
print("Hasil a yang ketiga: %d" %b)

#Kasus 2
x = 0
y = 1
z = x*2 + y*5
print(z)

#Kasus 3
a = 1
t = 3
l = 0.5*a*t
print("%g"%l)

#Kasus 4
V0 = 0
t = 12.5
Vt = 21.55
a = Vt / t - V0
print("%g"%a)
