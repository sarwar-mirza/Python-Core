#Append Method In Python

a = [10,20,12.4,-45,'Md Golam Sarwar']
n = len(a)
print("Befor Appending")
i = 0 
while(i<n):
    print("Index",i,'= ',a[i])
    i+=1


print()
print("Affter appending Method")
a.append(200)                          #Calling append() Method
x= len(a)
i = 0
while(i<x):
    print("Index",i,"= ",a[i])
    i+=1