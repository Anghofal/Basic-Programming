#Jumlah Murid
masukan = int(input("Masukkan Jumlah Murid : "))
#List Kosong
murid = []
# a disini nanti berfungsi untuk nomor murid
a = 0

#for disini untuk memasukkan jumlah list
for i in range (1,masukan+1) :
    #membuat variabel nama untuk mengisikan list murid
    nama = input("Inputkan nama murid yang ke-{} : ".format(i)) #jadi format i disini sesuai dengan range murid tadi yang dimasukkan 
    #fungsi list untuk menambahkan variabel nama sebelumnya
    murid.append(nama)
print("Jumlah murid = ",masukan,"anak")
print("Yaitu : ")
#untuk j didalam list murid yaitu [0,1]
for j in murid :
    a+=1
    print(a,". {}".format(j)) # sama saja seperti print(a,".",j)


    