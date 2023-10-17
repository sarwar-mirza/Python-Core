'''Set Comprehension
   List Comprehension represents creation of new list from an iterable object that satisfy a given condition.
   Syntex-> new_lst{expression for Item in Iterable_Object if_statement}

   Set Comprehension with if else Statement
   Syntax-> new_lst={expression if_statement else expression for i Item in Iterable_Object}
'''
'''
#Example-1
set1 = set()            # Empty set function
for i in range(20):
    set1.add(i+1)
#print(set1)

new_set = {i+1 for i in range(20)}   # Set Comprehension [work in ex-1]
print(new_set)'''


'''
#Example-2 with if statement
set1 = set()
for i in range(20):
    if(i%2==0):
        set1.add(i)
#print(set1)

new_set = {i for i in range(20) if i%2==0}   # Set Comprehension [work in ex-2]
print(new_set)'''

'''
#Example-3 with Nested if statement
set1 = set()
for i in range(20):
    if(i%2==0):
        if(i%3==0):
            set1.add(i)
#print(set1)

new_set = {i for i in range(20) if(i%2==0) if(i%3==0)}  # Set Comprehension [work in ex-3]
print(new_set)'''


#Example-4 with if else statment
set1 = set()
for i in range(10):
    if (i%2==0):
        set1.add(i)
    else:
        set1.add(i*1000)
        
#print(set1)

new_set = {i if i%2==0 else i*1000 for i in range(10)}    # if else Comperhension [work in ex-4]
print(new_set)
