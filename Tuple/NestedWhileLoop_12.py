# Nested While loop

a = (10,20,30,(40,50))
n= len(a)

i = 0
while(i<n):
    if type(a[i]) is tuple:
        x = len(a[i]) 
        if(x>1):
            y = len(a[i])
            j=0
            while(j<y):
                print(i,j,a[i][j])
                j+=1
            i+=1
    else:
        print(i,a[i])
        i+=1

print()


a = ((11,21,31),(41,51,61))
n = len(a)
i=0
while(i<n):
    j=0
    while(j<len(a[i])):
        print(i,j,"= ",a[i][j])
        j+=1
    i+=1
print()