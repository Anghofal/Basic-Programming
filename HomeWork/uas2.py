jumlah = 10
data = [77, 48,  2,  23,  33,  45,  56,  0,  86,  71] 

dicari = int(input('Data yang dicari: '))

posisi = -1
for indeks in range(0, jumlah):
    if data[indeks] == dicari:
        posisi = indeks
        break

if posisi == -1:
    print('Data tidak ditemukan')
else:
    print('Data ditemukan. Posisi pada indeks', posisi)