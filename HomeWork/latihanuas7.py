#isi list nya
A = [2,4,7,6,9]
B = [6,9,5,12,7]
# list tempat bilangan genap
isi_A = []
isi_B = []
# variabel untuk penambahan dari list bilangan genap
a = 0
b = 0
# untuk mengambil dari list  A secara berurutan
for i in A :
#untuk menyaring bilangan genap pada list A dan menambahkannya ke list isi_A
    if i % 2 == 0 :
        isi_A.append(i)
# menambahkan bilangan genap dari variabel i ke a
        a+=i
#untuk menyaring bilangan genap pada list B dan menambahkannya ke list isi_B
for j in B :
    if j % 2 == 0 :
        isi_B.append(j)
# menambahkan bilangan genap dari variabel j ke b
        b+=j
print("Maka Outputnya adalah : ",a,b)
print("Total Outputnya adalah :",a+b)