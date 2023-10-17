# Gatting Input From Users Using for Loop
from array import *
stu_roll = array('i', [])
n = int(input('Enter Number Of Elements for Loop : '))

for i in range(n):
    stu_roll.append(int(input('Enter Element : ')))

for i in range(len(stu_roll)):
    print('Index', i, '= ', stu_roll[i])



#Gatting Input From Users using while Loop

from array import *
stu_roll = array('i', [])
n = int(input('Enter Number Of Elements while Loop : '))

i=0
while (i<n):
    stu_roll.append(int(input('Enter Element : ')))
    i+=1

le = len(stu_roll)
j=0
while (j<le):
    print(stu_roll[j])
    j+=1

print('After Insert() method')

stu_roll.insert()