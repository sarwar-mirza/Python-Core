#Dictionary
a = {101:'sarwar', 102:'mithu',103:'salman', 104:'mehedi', 105:'sajada'}
for i in a:
    print(a[i])
print(id(a))
print("After Modifiying")
a[102]='Python'
a[101]='Programmer'
print(a)
print(id(a))
print()
print("After Adding")
a[106]='Java'
print(a)
print(id(a))
print()
print("After deleation")
del a[103]
print(a)
print(id(a))
print()
print("Exist in Dictionary")
print(103 in a)
print("*"*40)
print("copy Dictionary")
b = a.copy()
print(a, id(a))
print(b, id(b))
print("modifying B")
b[104]= 'HTML & CSS'
print(a, id(a))
print(b, id(b))
print()
print(b.get(102))
print()
print(a.items())
print()
lst = list(a.items())
print(lst)
print()
print(lst[0])
print(lst[0][0])
print(lst[0][1])
for r in lst:
    for j in r:
        print(j)
print()
print(b)
all_keys = b.keys()
print(all_keys)
for k in all_keys:
    print(k)
print()
print(a)
all_values = a.values()
print(all_values)
lst = list(all_values)
print(type(lst))
for val in lst:
    print(val)
print()
print(b)
b.update({103:"C++"})
print(b)
print()
returned = b.setdefault(107,'javascript')
print(returned)
user_input = {}
n = int(input("Enter Number Of Elements: "))
for ele in range(n):
    k = input("Enter Keys: ")
    v = input("Enter Values: ")
    user_input.update({k:v})
    print()
print(user_input)
for i in user_input:
    print(i,'=',user_input[i])

