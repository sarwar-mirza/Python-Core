'''This method returns an object that contains key-value pairs of dictionary.
   The pairs are stored as tuples in the object.
   Syntex-->dit_name.items()
'''

stu = {101:'Liza',102:'Lima',103:'Sarwar mithu'}
print('Orginal Dict ')
print(stu)
print(type(stu))
print()

new_stu = stu.items()   #items() method result dibe pair & Tuple
print(new_stu)
print(type(new_stu))
print()

lst = list(new_stu)       #Type convertion tuple to list
print(lst)
print(type(lst))
print()

for i in lst:
    for j in i:
        print(j)

