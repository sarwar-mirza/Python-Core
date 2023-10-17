# Using while() numpy Loop in python 

from numpy import *
n = int(input("Enter Number Of Elemnts : "))
a = zeros(n,dtype=int)

i = 0
while(i<n):
    x = int(input("Enter Element : "))
    a[i]=x
    i+=1

j=0
l = len(a)
while(j<l):
    print('index',j,'= ',a[j])
    j+=1