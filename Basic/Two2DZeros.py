#Using 2D zeros Function

from numpy import *
num1 = int(input("Enter Number Of Rows : "))
num2 = int(input("Enter Number Of Columns : "))

a = zeros((num1,num2),dtype= int)                     #Using zeros() Funcation
print(a)

n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        x = (int(input("Enter Of Element : ")))
        a[i][j] = x
    

for i in range(len(a)):
    for j in  range(len(a[i])):
        print("index",i,j,"= ",a[i][j])
    print()