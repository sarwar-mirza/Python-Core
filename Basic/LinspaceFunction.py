# Linspace() Function Syntex-> linspace(start,stop,num=50,endpoint=True,restep=False,dtype=Name,axis=0)

from numpy import *
a = linspace(1,8,5)         #1-8 pajonto shokake 5 vage vag kore dibe
n = len(a)
i=0
while(i<n):
    print('index',i,'= ',a[i])
    i+=1
