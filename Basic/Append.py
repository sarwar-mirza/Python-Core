# Append() Function [jukto kora ]

from array import * 
stu_roll = array('i', [101,102,103,104,105])

n = len(stu_roll)
i = 0
while (i<n):
    print('Index', i , '= ', stu_roll[i])
    i+=1


print('After Append() Function called')

stu_roll.append(106)          # Using append() Function 
stu_roll.append(107)          # Using append() Function
n = len(stu_roll)
for i in range(n):
    print('After Append Index ',i ,'= ', stu_roll[i])

print('Rest Of The append() Function for loop')
