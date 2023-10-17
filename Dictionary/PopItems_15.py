'''This method is used to removed the item which was last inserted into the dictionary.
   It returns the removed item in the form of TUPLE, Pairs are returned in LIFO Order.
   Syntex->dict_name.popitem()
'''

stu = {101:'Salman',102:'Sarwar',103:'Mehedi',104:'Liza'}
print("Before Deleting ")
print(stu)
print(id(stu))
print()

de_stu = stu.popitem()           #Last inserted delete in the dictionary
print("After Deleating")
print(stu)
print(id(stu))
print("Removing/delete Item : ",de_stu)
print()