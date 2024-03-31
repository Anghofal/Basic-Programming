batas = int(input("Masukkan bilangan : "))

for i in range(1,batas+1) :
    for j in range(1,batas+1):
        print(j,end="")
        if  j == batas :
            print("")
    for k in range(batas,0,-1) :
        print(k,end="")
        if k == 1 :
            print("")
