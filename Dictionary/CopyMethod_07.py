''' This method is used to copy all the elements from the existing dictionary into a new dictionary
    Syntex-> dict_name.copy()
'''

stu = {101:'Liza',102:'Lima',103:'Sarwar mithu'}
print('Before Copy')
print(stu)
print(id(stu))
print()


New_stu = stu.copy()      # Using copy() method
print("After Copied ")
print(New_stu)
print(id(New_stu))
print()