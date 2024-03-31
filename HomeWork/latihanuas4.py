bilangan = [77 ,48 ,2 ,23 ,33 ,45 ,56 ,0 ,86 ,71]
inputan = int(input("Data Yang dicari : "))
x = bilangan.index(inputan)
if x in bilangan :
    print("Data ada di indekx ke-",x)
elif x not in bilangan :
    print("salah")
