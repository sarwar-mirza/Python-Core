'''This method is used to update the dictionaray with the specified key value pair.
   Syntex-> dict_name.update(iterable)
'''

stu = {101:'Liza', 102:'Lima',103:'Sarwar'}
print("Before Upadting ",stu)
print(id(stu))
print(type(stu))
print()

stu.update({104:'Python Programming'})
print("After Updating ")
print(stu)
print(id(stu))
print(type(stu))
print()