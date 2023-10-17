# We can modify the existing value of key by assigning a new value
a = {101:'Sajada',102:'Abu Taher',103:'Mehedi', 104:'Salman',105:'Sarwar'}
print("Before Modification A :",a)
print(id(a))
print(type(a))
print()


a[105]= 'Python'
print("After Modification :",a)
print(id(a))
print(type(a))
print()