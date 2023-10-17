# Tuple of list

a = ([11,21],[31,41])
print("Orginal Tuple A: ",a)
print(id(a))
print(type(a))
print()

print("Accessing Tuple Of List for loop")
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,a[i][j])
    print()

x = (101,102,[104,105])
n = len(x)
for i in range(n):
    if type(x[i]) is list:
        m = len(x[i])
        if m>1:
            n = len(x[i])
            for j in range(n):
                print(i,j,x[i][j])
    else:
        print(i,x[i])
    print()