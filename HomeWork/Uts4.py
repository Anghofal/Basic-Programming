#Nomor 2
kolom = int(input("Masukkan Jumlah Kolom : "))
baris = int(input("Masukkan Jumlah Baris : "))
print("Masukkan nilai array","["+str(kolom)+"]","["+str(baris)+"]",":")
a = 0
while (a < baris) :
    a+=1
    b = 0
    print("")
    while (b < kolom) :
        b+=1
        print("Baris",a,"Kolom",b,":",end=" ")
        d = int(input())
        print(d)
        
