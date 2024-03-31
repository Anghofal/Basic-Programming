KoBa = int(input("Masukkan Kode Baju (1-5) : "))
if KoBa == 1 :
    print("Merk Baju = 3Second")
elif KoBa == 2 :
    print("Merk Baju = Nevada")
elif KoBa == 3 :
    print("Merk Baju = Gucci")
elif KoBa == 4 :
    print("Merk Baju = Louis Vuitton")
elif KoBa == 5 :
    print("Merk Baju = Kick Denim")
else :
    print("Salah Kode")
ukuran = str(input("Ukuran Baju (s/m/terserah) : "))
harga = 0
if KoBa == 1 and ukuran == "s" :
    harga += 200000
elif KoBa == 1 and ukuran == "m" :
    harga += 220000
elif KoBa == 1 :
    harga += 250000
    
if KoBa == 2 and ukuran == "s" :
    harga += 170000
elif KoBa == 2 and ukuran == "m" :
    harga += 180000
elif KoBa == 2  :
    harga += 200000

if KoBa == 3 and ukuran == "s" :
    harga += 200000
elif KoBa == 3 and ukuran == "m" :
    harga += 250000
elif KoBa == 3  :
    harga += 270000

if KoBa == 4 and ukuran == "s" :
    harga += 300000
elif KoBa == 4 and ukuran == "m" :
    harga += 300000
elif KoBa == 4  :
    harga += 350000

if KoBa == 5 and ukuran == "s" :
    harga += 100000
elif KoBa == 5 and ukuran == "m" :
    harga += 120000
elif KoBa == 5  :
    harga += 130000
print("Harga Baju :",harga)

JuBe = int(input("Jumlah Beli (1 - terserah) : "))
harga_jual = harga * JuBe
diskon = 0
if KoBa == 1 and JuBe > 3 :
    diskon += 1/2
elif KoBa == 2 and JuBe > 3 :
    diskon += 1/2
elif KoBa == 3 and JuBe > 3 :
    diskon += 4/10
elif KoBa == 4 and JuBe > 3 :
    diskon += 35/100
elif KoBa == 5 and JuBe > 3 :
    diskon += 45/100
harga_diskon = harga_jual * diskon
harga_total = harga_jual - harga_diskon
print("Total Harga:",harga_total)