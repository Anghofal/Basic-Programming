# How many Students
studentCounts = int(input("How many students you want to print the name : "))
# Empty array
students = []
# This var will be used later to be students number
a = 0

# For i = 1 until studentCounts+1
for i in range (1, studentCounts+1) :
    # Input the name of the students
    name = input("Students number "+ str(i) +" is : ")
    # Array function to add member
    students.append(name)

print("Students that in the array is = "+ str(studentCounts))
print("The names are : ")
# For each j in students
for j in students :
    a+=1
    print(a,". {}".format(j)) # Same like print(a,".",j)


    