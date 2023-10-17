#Getting List Input From User In Python

a = []
x = int(input("Enter Number Of Elements : "))

for i in range(x):
    a.append(input("Enter Element : "))            

print()
n = len(a)
for i in range(n):
    print("Index",i," =",a[i])

print()
print(a)
