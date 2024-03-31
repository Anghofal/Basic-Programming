print("1 . Sego")
print("2 . Mie")
print("3 . Bakso")
print("4 . Soto")
# return = hasil pemrosesan
# 
i = int(input("Masukkan Nilai : "))
def pilihan(i) :
    if i == 1 : 
        return("sego") 
    elif i == 2 : 
        return("Mie")
    elif i == 3 :
        return("Bakso")
    elif i == 4 :
        return("Soto")
    else :
        return("salah")
print(pilihan(i))
