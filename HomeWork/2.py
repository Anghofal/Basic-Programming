#Kasus 1
a = 0
b = 4.5
c = "kata"

print("Latihan 1\n")
print(type(a))
print("\tNilai bilangan bulat a adalah",a,"\n")
print(type(b))
print("\tNilai bilangan decimal b adalah",b,"\n")
print(type(c))
print("\tKata dari c adalah",c,"\n")

#Kasus 2
umur = 18
berat_badan = 48.3

print("umur saya",umur,"tahun")
print("umur saya",umur)
print("umur saya",str(umur)+"tahun")
print("umur saya %d "%(umur))
print("berat badan saya %g"%(berat_badan))
print("berat badan saya {} Kg".format(umur),"\n")

# Kasus 3
Ayah ="Eko"
Ibu = "Joni"

print("ayah mawar adalah :",Ayah)
print("ibu mawar adalah :",Ibu)

#Kasus 4
a = 1
b = 4

print("Hasil a yang pertama:",a)
print("Hasil b yang pertama: "+str(b))

b = a + 1
a = a - b
print("Hasil a yang kedua: "+str(a))
print("Hasil b yang kedua:",b)

a = b + 2
b = a * b 

print("Hasil a yang ketiga:{}".format(a))
print("Hasil b yang ketiga: %f"%b)

c = a
a = b 
b = c

print("Hasil a yang keempat: {}".format(a))
print("Hasil b yang keempat: {}".format(b))
print("Hasil c yang keempat: {}".format(c))
 