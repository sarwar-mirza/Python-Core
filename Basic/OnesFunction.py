# ones() Function Syntex-> numpy.ones(shape,dtype=float,order='C)


from numpy import *
a = ones(5)
n = len(a)
i = 0
while(i<n):
    print('index',i,'= ',a[i])
    i+=1