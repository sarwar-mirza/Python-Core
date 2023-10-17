# Nested For loop

a = (10,20,30,(40,50))

n = len(a)
for i in range(n):
    if type(a[i]) is tuple:
        x = len(a[i])
        if(x>1):
            y = len(a[i])
            for j in range(y):
                print(i,j,a[i][j]) 


    else:
        print(i,a[i])
print()



a = ((101,201,301),(401,501,601))
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,"= ",a[i][j])
    print()