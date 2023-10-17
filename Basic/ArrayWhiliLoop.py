# Accessing Array Using While Loop
from array import *
stu_roll = array('i', [101,102,103,104,105])

n = len(stu_roll)
i = 0
while (i<n):
    print('Index', i , '= ', stu_roll[i])
    i+=1
print('Rest Of The Accessing While Loop Code')