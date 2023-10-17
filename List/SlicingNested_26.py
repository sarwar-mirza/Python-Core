# Slicing Nested loop
x = [[10,20,30],[40,50,60],[70,80,90],[11,22,33],[44,55,66],[77,88,99],[12,13,14]]

print("Orginal Nested Loop")
print(x)
print()

print("From 1st Postion To 4th Positio")
a = x[1:5]
print(a)
print()

print("From 0th Position To 6th Position")
b = x[0:]
print(b)
print()

print("From 0th Postion To 4th Position")
c = x[:5]
print(c)
print()

print("Last 4 List")
d = x[-4:]
print(d)
print()

print("From 0th Position To 6th Position Stepsize 2")
e = x[0:7:2]
print(e)
print()

print("Last 5 List With [-5-(-3)]= 2 List twoards right")
f = x[-5:-3]
print(f)
print()

print("***********************************")
print("Slice Nested 2nd Postion, 0th Postion")
g = x[2:3]
print(g)
h = x[2:3][0]
print(h)
print()

print("Slice 2nd List Then Extract Elements")
#Extracting Only One Element
i = x[2:3][0][0]
print(i)
#Extraction Only All Elements
j= x[2:3][0]
for el in j:
    print(el)
print()

print("Last Nested 4 List Then 1st Postion")
k = x[-4:]
print(k)
l = x[-4:][1]
print(l)
print()

print("Last Nested 4 List Then 1st position Then Extract Elements")
m = x[-4:][1][0]
print(m)
n = x[-4:][1]
for i in n:
    print(i)
print()