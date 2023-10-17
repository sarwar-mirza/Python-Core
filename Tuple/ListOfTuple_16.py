# List Of Tuple

a = [10,20,(30,40)]                # Create List Of Tuple
print("Orginal List A : ",a)
print(id(a))
print(type(a))
print()

print("Appending a new Tuple ")
a.append((50,60))
print("After Appending A : ",a)
print(id(a))
print(type(a))
print()

print("********************")
print("Accessing List Of Tuple For Loop")
n = len(a)
for i in range(n):
    if type(a[i]) is tuple:                     #Check this condition what is this type
        x = len(a[i])
        if x>1:
            m = len(a[i])
            for j in range(m):
                print(i,j,':',a[i][j])
    else:
        print(i,':',a[i])
print()

print('List Of Tuple')

a = [(11,22),(33,44)]
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,a[i][j])
    
