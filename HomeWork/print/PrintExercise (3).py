# Case 1
a = 1
print("a is : " +str(a))
b = 4
print("b is : " +str(b))

b = a
print("variable b is now equal to a, variable b is now: " +str(b))
a -= b
print("variable a is now equal to b minus 1 (1 - 1), variable a is now: " +str(a))

a = b + 1
print("variable a is now equal to variable b + 1 (1 + 1), variable a is now: " +str(a))
b = a / b
print("variable b is now equal to variable a divided by b (2 / 1), variable b is now : %d" %b)

# Case 2
x = 0
y = 1
z = x*2 + y*5
print(z)

# Case 3
a = 1
t = 3
l = 0.5*a*t
print("%g"%l)

# Case 4
V0 = 0
t = 12.5
Vt = 21.55
a = Vt / t - V0
print("%g"%a)
