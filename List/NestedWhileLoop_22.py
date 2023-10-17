# Nested While Loop

a = [10,20,30,[40,50]]         #First awy Nested loop
n = len(a)
i = 0
while(i<n):
    if type(a[i]) is list:
        x = len(a[i])
        if(x>1):
            m = len(a[i])
            j=0
            while(j<m):
                print(i,j,'=',a[i][j])
                j+=1
            i+=1
    
    else:
        print(i,'=',a[i])
        i+=1
print()


x = [[110,120,130],[140,150,160]]
n = len(x)
i = 0
while(i<n):
    j=0
    while(j<len(x[i])):
        print(i,j,'=',x[i][j])
        j+=1
    i+=1

