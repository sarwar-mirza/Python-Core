# slicing() --> new_array_name = array_name[start:stop:stepsize, start:stop:stepsize]


from numpy import*
a = array([[1,2,3],
           [4,5,6],
           [7,8,9]])

print("Orginal Array")
print(a)
n= a[0:2, 1:3]
print(n)

n= a[:, 0]
print(n)
print()
n= a[2, :]
print(n)
n= a[0:1, 0:1]
print(n)




from numpy import *
num1 = int(input("Enter Number Of Rows : "))
num2 = int(input("Enter Number Of Columns : "))

a = zeros((num1,num2), dtype=int)
print(a)

n = len(a)
i = 0 
while(i<n):                                     #User Using input in while() loop
    j=0
    while(j < len(a[i])):
        x = int(input("Enter Element : "))
        a[i][j] = x
        j+=1
    i+=1



i = 0                          #Output in while() loop
n2 = len(a)
while(i<n2):
    j=0
    while(j<len(a[i])):
        print('Index',i,j,'= ',a[i][j])
        j+=1
    i+=1
    print()
print(a)

