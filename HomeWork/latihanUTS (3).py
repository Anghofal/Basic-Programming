bilangan = int(input("Inputkan Bilangan : "))
a = 0
while (a < bilangan) :
    a+=1
    print(a,"=",a)
    if a == 1 :
        break
b = 1
while (b < bilangan) :
    b+=1
    c = a + b
    print(a,"+",b,"=",c)
    if b == 2 :
        break
d = 2
while (d < bilangan) :
    d+=1
    c = a + b + d
    print(a,"+",b,"+",d,"=",c)
    if d == 3 :
        break
e = 3
while (e < bilangan) :
    e+=1
    c = a + b + d + e
    print(a,"+",b,"+",d,"+",e,"=",c)
    if e == 4 :
        break
