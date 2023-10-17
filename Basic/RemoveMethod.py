# remove() Method Syntex--> array_name.remove(Element)


from array import * 
stu_roll = array('i', [])

n = int(input('Enter Number Of Elements : '))
i = 0
while (i<n):
    stu_roll.append(int(input('Enter Element : ')))
    i+=1

j = 0
a = len(stu_roll)
while(j<a):
    print('Index',j,'= ',stu_roll[j])
    j+=1


print("After Using remove() Method ")

re = int(input("How Many Remove Elements : "))
i = 0
while(i<re):
    stu_roll.remove(int(input('Select Elements :')))        #Useing remove() Method [index na elements removie hobe]
    i+=1

j = 0
r = len(stu_roll)
while(j<r):
    print("New Index After Removing",j,'= ',stu_roll[j])
    j+=1
