class Kalender:
    print("Aplikasi Validasi Tanggal")
    print("Masukkan Tanggal")
    tanggal = int(input())
    print("Masukkan Bulan")
    bulan = int(input())
    print("Masukkan Tahun")
    tahun = int(input())

    if(bulan == 1):
        hari = 31
        namaBulan = "Januari"
    elif(bulan == 2):
        # Membuat Tahun Kabisat

        if((tahun % 4 == 0 and tahun % 100!=0) or tahun % 400 == 0):
            hari = 29
        else:
            hari = 28
            namaBulan = "Februari"
    elif(bulan == 3):
        hari = 31
        namaBulan = "Maret"
    elif(bulan == 4):
        hari = 30
        namaBulan = "April"
    elif(bulan == 5):
        hari = 31
        namaBulan = "Mei"
    elif(bulan == 6):
        hari = 30
        namaBulan = "Juni"
    elif(bulan == 7):
        hari = 31
        namaBulan = "Juli"
    elif(bulan == 8):
        hari = 30
        namaBulan = "Agustus"
    elif(bulan == 9):
        hari = 31
        namaBulan = "September"
    elif(bulan == 10):
        hari= 30
        namaBulan = "Oktober"
    elif(bulan == 11):
        hari = 31
        namaBulan = "November"
    elif(bulan == 12):
        hari = 30
        namaBulan = "Desember"
    else:
        hari = -1
        namaBulan = bulan

    bTanggal = tanggal >=1 and tanggal <= hari
    bBulan = bulan >=1 and bulan <=12
    bValid = bTanggal and bBulan

    if(bValid):
        hasil = " adalah tanggal yang valid."
    else:
        hasil = " adalah tanggal yang tidak valid."

    print("%d %s %d %s"%(tanggal,bulan,tahun,hasil))