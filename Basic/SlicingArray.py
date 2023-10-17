# slicing[] Array Syntex--> slicing[start:stop:stepsize]

from array import *
stu_roll = array('i',[101,102,103,104,106,107,108])
print('Orginal Array')
n = len(stu_roll)
for i in range(n):
    print(i, '= ',stu_roll[i])

print('After Silicing *******************')

a = stu_roll[2:6]
for i in a:
    print(i)