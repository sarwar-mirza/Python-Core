# extend() Method Syntex --> array_name.extend(another_array_name)

from array import *
stu_roll = array('i', [])
n = int(input('Enter Number Of 1st Elements : '))

for i in range(n):
    stu_roll.append(int(input('Enter Element : ')))

for j in range(len(stu_roll)):
    print('Index', j,'= ',stu_roll[j])

print('After using extend() Method ')

stu_roll2 = array('i', [])
n2 = int(input('Enter Number of 2nd Elemnts : '))

for i in range(n2):
    stu_roll2.append(int(input('Elements : ')))

stu_roll.extend(stu_roll2)                          #Using extend() Method [duiti bhinno array ke jog kora]
for j in range(len(stu_roll)):
    print('Totaal Index',j,'= ', stu_roll[j])