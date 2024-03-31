biji = int(input("Masukkan Jumlah Biji Coklat : "))
permen = biji * 12
kotak = permen % 5
print("Jumlah Kotak Coklat Yang Dapat Dijual :",kotak)
if permen % 5 == 1 :
    print("Sisa permen coklat yang tidak dapat dikemas dalam kotak : 1")
elif permen % 5 == 2 :
    print("Sisa permen coklat yang tidak dapat dikemas dalam kotak : 2")
elif permen % 5 == 3 :
    print("Sisa permen coklat yang tidak dapat dikemas dalam kotak : 3")
elif permen % 5 == 4 :
    print("Sisa permen coklat yang tidak dapat dikemas dalam kotak : 4")