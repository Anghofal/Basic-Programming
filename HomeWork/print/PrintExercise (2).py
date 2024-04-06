# Case 1
a = 0
b = 4.5
c = "isAWord"

print("Exercise 1\n")
print(type(a))
print("\tThe integer value of a is",a,"\n")
print(type(b))
print("\tThe value of the decimal number b is",b,"\n")
print(type(c))
print("\tThe word for c is",c,"\n")

# Case 2
age = 18
bodyWeight = 48.3

print("my age is",age,"tahun")
print("my age is",age)
print("my age is",str(age)+"tahun")
print("my age is %d "%(age))
print("my body weight is %g"%(bodyWeight))
print("my body weight is {} Kg".format(age),"\n")

# Case 3
dadIsName ="Eko"
momIsName = "Joni"

print("mawar's father name is :",dadIsName)
print("mawar's mother name is :",momIsName)

# Case 4
a = 1
print("variable a is :",a)

b = a + 1
print("Now variable b is variable a added by 1 (1+1):",b)

a = a - b
print("Now Variable a is equal variable a minus b (1 - 2): "+str(a))

a = b + 2
print("On the third times variable a is now b + 2 (2 + 2): {}".format(a))

b = a * b 
print("On the third times variable b is now equal to a times b (4 * 2): %f"%b)

c = a
print("On the fourth times variable c now is equal to a, variable c is: {}".format(c))
a = b 
print("On the fourth times variable a now is equal to b, variable a is: {}".format(a))
b = c
print("On the fourth times variable b now is equal to c, variable b is: {}".format(b))