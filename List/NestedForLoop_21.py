# Nested For Loop

a = [10,20,30,[40,50]]                        # First awy to Nested Loop

n = len(a)
for i in range(n):
    if type(a[i]) is list:              #Checking a[i] is a list type or not
        x = len(a[i])
        if x>1:
            m = len(a[i])
            for j in range(m):
                print(i, j,'=',a[i][j])
    else:
        print(i,'=',a[i])
print()



x = [[110,120,130],[140,150,160]]                             #Second awy Nested Loop
n = len(x)
for i in range(n):
    for j in range(len(x[i])):
        print(i,j,'= ',x[i][j])
print()