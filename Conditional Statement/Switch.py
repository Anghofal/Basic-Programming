print("1 . Fried Rice")
print("2 . Indomi Goreng")
print("3 . Bakso")
print("4 . Soto")


i = int(input("Enter Value : "))
def YourFoodIs(i) :
    if i == 1 : 
        return("Fried Rice")
    elif i == 2 : 
        return("Indomi Goreng")
    elif i == 3 :
        return("Bakso")
    elif i == 4 :
        return("Soto")
    else :
        return("salah")
print(YourFoodIs(i))
