# numpy array Syntex--> array_name= array([elements])


from numpy import *
stu_roll = array([101,102,103,104,105])
print(stu_roll)
print(stu_roll.dtype)

stu_roll[2]= 123      # Modifay in Python Code
n = len(stu_roll)
for i in range(n):
    print('index',i,'= ',stu_roll[i])


print('*****While Loop******')
i=0
while (i<n):
    print('Index',i,'= ',stu_roll[i])
    i+=1