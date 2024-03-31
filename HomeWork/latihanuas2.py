bulan = ["tambahan","Januari", "februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September","Oktober","November","Desember"]
inputan = int(input("Masukkan Nilai 1-12 : "))
if (inputan <= 0) or (inputan > 12) :
    print("Range Inputan Harus 1-12")
else :
    print(bulan[inputan])