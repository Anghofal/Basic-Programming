# 3 . If Elif Else
print("")
x = int(input("Enter Your Number : "))

#Algoritma
if (x % 2 == 0) and (x % 3 == 0) :
    print("Your number is multiple of 2 and 3")
elif x % 2 == 0 :
    print("Your number is multiple of 2")
elif x % 3 == 0  :
    print("Your number is multiple of 3")
else :
    print("Your number is not multiple of 2 or 3")