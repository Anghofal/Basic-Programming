#coro gampange full tree
#def tree(n):
#z = n - 1
#x = 1
#for i in range(n):
#    print(' ' * z + '+' * x + ' ' * z)
#    x+=2
#    z-=1
#tree(5)

#full tree gawean ku
tinggi = int(input("Masukkan Tinggi : "))
kosong = tinggi - 1
titik = 1
for i in range(tinggi) :
    print(" "*kosong,"*"*titik," "*kosong)
    titik+=2
    kosong-=1

