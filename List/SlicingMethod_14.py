#Slicing -->New_list_Name=list_name[start:stop:stepsize]

x = [101,102,103,104,105,106,107]
print("Orginal Arrar ",x)


print("From 1st Position to 4th Position")
a = x[1:4]
for i in a:
    print(i)
print()

print("From 1th Position to last Position")
b = x[0:]
for i in b:
    print(i)
print()

print("From 0th Position to 4th Position")
c = x[:4]
for i in c:
    print(i)
print()

print("Last 4 Elements")
d = x[-4:]
for i in d:
    print(i)
print()

print("From 0th Position to 6th Position Stepsize 2")
e = x[0:6:2]
for i in e:
    print(i)
print()

print("Last 5 Elements with [-5-(3)]= 2 elements towards right")
f = x[-5:-3]
for i in f:
    print(i)
print()
