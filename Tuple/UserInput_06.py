''' Getting input from user in Tuple
    Tuple input neoa khub complicate tai amra prothome list input nibo then tuple convert kore dibo '''

a = []
n = int(input("Enter Number Of Elements :"))

for i in range(n):                               #User input
    a.append(input("Enter Elements :"))


print(a)
print(type(a))
print()

print("List to Tuple convert")
a = tuple(a)                               #List to tuple conversion
print(a)
print(type(a))
print()


for j in range(len(a)):
    print(j,'= ',a[i])
print()
