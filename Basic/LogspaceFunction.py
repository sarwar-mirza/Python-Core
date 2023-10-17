#logspace() Function Syntex->numpy.logspace(start,stop,num=50,endpoint=True,base=10,dtype=None,axis=0)

from numpy import *
a = logspace(1,3,num=5,base=12)   #base power strt ebong base power stop ex-12^1(start) ebong 12^3(stop)

n= len(a)
for i in range(n):
    print('index',i,'= ',a[i])