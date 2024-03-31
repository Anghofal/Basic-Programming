string=input("masukkan string:")
length=len(string)
a=0
for i in range (length):
	for j in range(i):
		print('',end=' ')
	for j in range (a,length):
		print(string[j],end='')
	a+=1
	print()
