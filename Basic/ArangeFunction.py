# arange() Function Syntex->numpy.arange(start,stop,stepsize,dtype=None)

from numpy import*
a = arange(1,10,2)                #a = arange(,10)stop likhe dilei hobe 0-9 count kore dibe

n= len(a)

for i in range(n):
    print('Index', i,'= ',a[i])