'''This method returns the value of the specified key.
    If key is not found then it will return none or default value.
    Syntex-> dict.get(key,default_value)
'''


stu = {101:'Liza',102:'Lima',103:'Sarwar mithu'}
print('Orginal Dict')
print(stu)
print()

print(stu.get(101))       #return specified key
print()

print(stu.get(104))       #This key doesn't exist
print()

print(stu.get(104, 'Pyhon Code'))  #This key doesn't exist but vlaue return using get METHOD
print()