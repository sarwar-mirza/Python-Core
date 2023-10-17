# User numpy array input in python 

from numpy import *
n = int(input('Enter Number Of Elements : '))
a = zeros(n, dtype=int)

for i in range(len(a)):
    x = int(input('Enter Element : '))
    a[i] = x

for j in range(len(a)):
    print('index',j,'= ',a[j])