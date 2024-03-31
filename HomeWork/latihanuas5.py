# start awal dari 1
x = 1
# stop di angka 10
y = 11
#step awalnya satu
z = 1

# di print ke 3 gunanya untuk menambahkan jumlah start dan step
for i in range(4) :
# di print ke 2 gunanya untuk enter / spasi ke bawah karena ada end=""
    for j in range(1) :
# di print pertama digunakan untuk print angka 1 sampai sepulah dan jumlah start dan step nya bertambah karena print ke 3
        for k in range(x,y,z) :
            print(k,end=" ")
        print()
    x+=1
    z+=1
        
