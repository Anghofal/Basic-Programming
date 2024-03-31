#list kosong agar nanti bisa ditambah
inputan = int(input("Jumlah Bilangan : "))
bilangan = []
#variabel jum untuk ditambah-tambah oleh variabel nilai nanti
jum = 0
print("Masukkan 10 data bilangan bulat")

#for disini untuk Mencetak variabel nilai
for i in range(1,inputan+1):
    #untuk mencari rata2
    nilai = int(input("Bilangan Ke-{} : ".format(i)))
    jum+=nilai
    rata2 = jum / 4
    #untuk menyaring bilangan lalu dimasukkan ke list bilangan
    if nilai > rata2 :
        bilangan.append(nilai)
print("rata-rata : ",rata2)
print("nilai yang diatas rata-rata adalah : ")
for bil in (bilangan):
    print("-",bil)
