# pop() Method Syntex--> array_name.pop()      [seser element delete hobe automaticly]

# array_name.pop(Positon_Number)         [nidusto element delete hobe]

from array import*
stu_roll = array('i', [])
n = int(input('Enter Number Of Elements : '))
for i in range(n):
    stu_roll.append(int(input("Enter Element : ")))

for j in range(len(stu_roll)):
    print('Index ',j,'= ', stu_roll[j])

print('After Pop() Method Using')

a = (int(input("How Many Delete Array : ")))
for p in range(a):
    stu_roll.pop(int(input("Position Number : ")))     #Applaying pop() Method [index select kore ta delete korbo]
    


for i in range(len(stu_roll)):
    print('New Index',i,'= ',stu_roll[i])