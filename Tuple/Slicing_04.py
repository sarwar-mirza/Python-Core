# slicing[]--> New_Tuple_Name[start:stop:stepsize]

x = (101,102,103,104,105,106,107)
print("Orginat Tuple")
print(x)
print(type(x))
print()

print("From 1st Position to 4th Position")
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

print('From 0th Position to 6th Position Stepsize 2 ')
f = x[0:7:2]
print(f)
print()

print("Last 4 List Element")
d = x[-4:]
print(d)
print()

print("Last 5 List With [-5-(-3)]=2 List Twoards Right")
e = x[-5:-3]
print(e)
print()