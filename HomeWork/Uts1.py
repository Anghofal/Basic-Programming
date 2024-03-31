x = int(input("Masukkan Nilai 1 = "))
y = int(input("Masukkan Nilai 2 = "))
z = int(input("Masukkan Nilai 3 = "))

print("Ket : (1) Penjumlahan (2) Pengurangan")

Operasi1 = int(input("Masukkan Operasi ke-1 = "))
Operasi2 = int(input("Masukkan Operasi ke-2 = "))

a = x + y + z
b = x - y + z
c = x + y - z
cc = x - y - z
if(Operasi1 == 1 and Operasi2 == 1 ) :
    print("Hasil =",x,"+",y,"+",z,"=",a,end=" ")
elif(Operasi1== 2 and Operasi2 == 1) :
    print("Hasil =",x,"-",y,"+",z,"=",b,end=" ")
elif(Operasi1== 1 and Operasi2 == 2) :
    print("Hasil =",x,"+",y,"-",z,"=",c,end=" ")
elif(Operasi1==2 and Operasi2== 2) :
    print("Hasil =",x,"-",y,"-",z,"=",cc,end=" ")     

if (a and b and c and cc) % 2 == 0 :
    print("( Bilangan Genap " , end="")
    if (a and b and c and cc) >= 0 :
        print("Positif )")
    elif (a and b and c and cc) <= 0 :
        print("Negatif )")
if (a and b and c and cc) % 2 == 1 :
    print("Bilangan Ganjil " , end="")
    if (a and b and c and cc) >= 0 :
        print("Positif )")
    elif (a and b and c and cc) <= 0 :
        print("Negatif )")


        

