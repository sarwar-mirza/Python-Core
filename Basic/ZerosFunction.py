# zeros() Function Syntex-> numpy.zeros(shape,dtype=float,order='C)


from numpy import *
a = zeros(5)
n = len(a)
i = 0
while(i<n):
    print('index',i,'= ',a[i])
    i+=1