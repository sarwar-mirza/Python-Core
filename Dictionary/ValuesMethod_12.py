'''This method returns a sequence of Values from the dictionry
   Syntex-> dict_name.values()
'''

stu = {101:'Liza',102:'Lima',103:'Sarwar'}
print(stu)
print(type(stu))
print()


all_value = stu.values()   #Applying  values() method
print(all_value)
print(type(all_value))
print()

value_lst = list(all_value)  # Tuple to list convert
print(value_lst)
print(type(value_lst))
print()
for i in value_lst:
    print(i)