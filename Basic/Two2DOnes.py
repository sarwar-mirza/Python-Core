# Using ones() Funcation


from numpy import *
num1 = int(input("Enter Number Of Rows : "))
num2 = int(input("Enter Number Of COlumns : "))

a = ones((num1,num2), dtype=int)                       #Applying ones() Funcation
print(a)
n = len(a)
i = 0
while(i<n):                                           #Applying Nested while() Loop and User input
    j=0
    while(j<len(a[i])):
        x = int(input("Enter Element : "))
        a[i][j] = x
        j+=1
    i+=1

i = 0                                                #Applying Nested while() Loop in Output
n2 = len(a)
while(i<n2):
    j = 0 
    while(j<len(a[i])):
        print("Index",i,j,'= ', a[i][j]) 
        j+=1
    i+=1
    print()
