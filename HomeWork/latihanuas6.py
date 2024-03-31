#list kosong digunakan untuk memasukkan nilai nanti
listkolom = []
baru = []
#inputan untuk baris dan kolom
baris = int(input("masukkan baris : "))
kolom = int(input("masukkan kolom : "))
panjanglist = baris * kolom
print("Array[",baris,"]","[",kolom,"]")
x = 0
# untuk mencetak nomor baris ke i
for i in range (1,baris+1) :
#untuk mencetak kolom ke j dan untuk mencetak input    
    for j in range(1,kolom+1) :
        print("Masukkan Baris Ke-",i,"Kolom Ke-",j,": ",end=" ")
        barkol = int(input())
        listkolom.append(barkol)

for k in range(0,panjanglist,kolom) :
    baru.extend(listkolom[0+x:kolom+k])
    print("list baru :",baru)
    for l in baru :
        print(l)
        x+=kolom