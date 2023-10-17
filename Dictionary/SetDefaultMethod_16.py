'''This Method returns the value of the specified key.
   If key is not found then it inserts key with the specified value.
   Syntax->dict_name.setdefault(key, value)
'''

stu = {101:'Liza',102:'Lima',103:'Sarwar'}
print("Orginal Dictionay ")
print(stu)
print(id(stu))
print()

returned_value = stu.setdefault(104,'Python')
print("After Setdefault value")
print(stu)
print(id(stu))
print('Returned Value : ',returned_value)
print()

