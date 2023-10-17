'''This method returns a sequence of keys from the dictionry
   Syntex-> dict_name.keys()
'''
stu = {101:'Liza',102:'Lima',103:'Sarwar mithu'}
print('Orginal Dict')
print(stu)
print(type(stu))
print()

all_keys = stu.keys()     #applying keys() method
print(all_keys)
print(type(all_keys))
print()

keys_lst = list(all_keys)  #Convert Tuples to list
print(keys_lst)
print(type(keys_lst))
print()