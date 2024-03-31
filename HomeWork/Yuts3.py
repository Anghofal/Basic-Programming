nama = str(input("Nama = "))
ipk = float(input("IPK = "))
akreditasi = str(input("Akreditasi Universitas = "))
if ipk < 3 or akreditasi != "A" :
    print("Mohon Maaf Saudara",nama,"anda tidak diterima")
elif ipk >= 3 and akreditasi == "A" :
    ta = int(input("Tes Akademik = "))
    tk = int(input("Tes Ketrampilan = "))
    tp = int(input("Tes Potensial = "))
    rata2 = (ta+tk+tp)/3
    print("Nilai rata-rata =",rata2)
    if rata2 < 85 :
        print("Mohon Maaf",nama,"anda tidak dapat diterima , karena nilai rata-rata tes dibawah 85")
    elif ta < 80 :
        print("Mohon Maaf",nama,"anda tidak dapat diterima , karena ada nilai tes dibawah 80")
    elif tk < 80 :
        print("Mohon Maaf",nama,"anda tidak dapat diterima , karena ada nilai tes dibawah 80")
    elif tp < 80 :
        print("Mohon Maaf",nama,"anda tidak dapat diterima , karena ada nilai tes dibawah 80")
    elif (ta > tk and tp) :
        print("Selamat",nama,"anda diterima, dan ditempatkan di bagian manajemen")
    elif (tk > ta and tp) :
        print("Selamat",nama,"anda diterima, dan ditempatkan di bagian produksi")
    else :
        print("Selamat",nama,"anda diterima, dan ditempatkan di bagian pemasaran")



