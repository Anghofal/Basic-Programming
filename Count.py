#Nama = Muhammad Tegar
#NIM = A11.2020.12782

def buatPerkalian(a):
    def kalikan (b):
        return a*b
    return kalikan

def buatPembagian(a):
    def bagikan (b):
        return a/b
    return bagikan

def main():
    kali5 = buatPerkalian (10)
    print (kali5(10))
    bagi10 = buatPembagian (5)
    print (bagi10(2))
if __name__ == "__main__" :
    main()