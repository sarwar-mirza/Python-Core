'''This method is used to remove the item with specified key.
   It returns the removed item's value
   If key is not found then the a default value is returned.
   Syntex-> dict_name.pop(key,default_value)
'''

stu = {101:'Liza',102:'Lima',103:'Sarwar'}
print("Orginal Dictionary")
print(stu)
print(id(stu))
print()

rem = stu.pop(102)
print("After Removing Dictionay")
print(stu)
print(id(stu))
print("Removed Value : ",rem)     # Returns the removed item's value
print()