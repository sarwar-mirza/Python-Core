# Two dimensional array using for loop
from numpy import*
a = array([[10,20,30,40],
           [50,60,70,80]])

n = len(a)

for i in range(n):
    for j in range(len(a[i])):
        print('Index ',i,j,'= ',a[i][j])
    print()