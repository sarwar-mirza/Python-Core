# Slicing Nested Tuple
x = ((10,20,30),(40,50,60),(70,80,90),(11,22,33),(44,55,66),(77,88,99),(12,13,14))
print("Orginal Tuple")
print(x)
print()

print("From 1st Position To 4th Position")
a = x[1:5]
print(a)
print()

print("From 0th Position To Last Position")
b = x[0:]
print(b)
print()

print("From 0th Position To 4th Position")
c = x[:5]
print(c)
print()

print("Last 4 Tuple")
d = x[-4:]
print(d)
print()

print("From 0th Position To 6th Position Stepsize 2")
e = x[0:7:2]
print(e)
print()

print("Last 5 Tuple With [-5-(-3)]=2 Tuple Twoards Right")
f = x[-5:-3]
print(f)
print()

print("*******************************")

print("Slice Nested 2nd Position. 0th Position")
g = x[2:3]
print(g)
h = x[2:3][0]
print(h)
print()

print("Slice 2nd Tuple Then Extract Elements")
i = x[2:3][0][0]
print(i)
j = x[2:3][0]
for i in j:
    print(i)
print()

print("Last Nested 4 Tuples Then 1st Position")
k = x[-4:]
print(k)
l= x[-4:][1]
print(l)
print()

print("Last Nested 4 Tuples Then 1st Position Then Extract Elements")
m = x[-4:][1][0]
print(m)
n= x[-4:][1]
for i in n:
    print(i)
print()