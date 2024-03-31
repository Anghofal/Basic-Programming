Nama = input("Masukkan Nama Pembeli : ")
KS = int(input("Masukkan Kode Susu (1/2/3) : "))
Uk = str(input("Masukkan Kode Ukuran (S/M/L) : "))
Jumlah = int(input("Masukkan Jumlah Beli : "))
harga = 0

if KS == 1 :
    if Uk == "S" :
        harga += 5000
    elif Uk == "M" :
        harga += 7500
    elif Uk == "L" :
        harga += 9500
if KS == 2 :
    if Uk == "S" :
        harga += 4500
    elif Uk == "M" :
        harga += 6500
    elif Uk == "L" :
        harga += 8500
if KS == 3 :
    if Uk == "S" :
        harga += 9500
    elif Uk == "M" :
        harga += 15500
    elif Uk == "L" :
        harga += 19500

Pembayaran = Jumlah * harga
Pajak = Pembayaran + Pembayaran * 1/10
Potongan = Pembayaran - Pembayaran * 1/20
TPembayaran = Pembayaran + Pajak - Potongan

print("Nama Pembeli : ",Nama)
print("Merk Barang : ",KS)
print("Jenis Ukuran : ",Uk)
print("Jumlah Beli : ",Jumlah)
print("Harga Barang : Rp.",harga)
print("Jumlah Pembayaran : Rp.",Pembayaran)
print("Potongan : Rp.",Potongan)
print("Pajak : Rp.",Pajak)
print("Total Pembayaran : Rp.",TPembayaran)
    