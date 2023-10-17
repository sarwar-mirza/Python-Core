# index() Method Syntex --> array_name.index(element)

from array import *
stu_roll = array('i', [101,102,103,101,104,105])
print(stu_roll.index(103))                       # index() position bole dibe koto no positione ace

#After revers() metod useing 
#Syntex --> array_name.revers()

print('After revers() Method Using')

stu_roll.reverse()
n = len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1