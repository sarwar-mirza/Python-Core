'''List Comprehension
   List Comprehension represents creation of new list from an iterable object that satisfy a given condition.
   Syntex-> new_lst[expression for Item in Iterable_Object if_statement]

   List Comprehension with if else Statement
   Syntax-> new_lst=[expression if_statement else expression for i Item in Iterable_Object]
'''
'''
#Example-01
lst1 = []
for i in range(20):
    lst1.append(i+1)
#print(lst1)
print()

#or
new_lst = [i+1 for i in range(20)]  #List Comprehension [Work in example-1]
print(new_lst)'''

'''
#Example-2
lst = []
for i in range(20):
    if (i%2==0):
        lst.append(i)
#print(lst)

new_lst= [i for i in range(20) if i%2==0]     #List comprehension [Work in example-2]
print(new_lst)'''

'''
#Example-3
lst = []
for i in range(20):
    if (i%2==0):
        if (i%3==0):
            lst.append(i)
#print(lst)

new_lst = [i for i in range(20) if(i%2==0) if(i%3==0)]  #List Comprehension [Work in exmaple-3]
print(new_lst)'''


#Example-4
lst = []
for i in range(10):
    if (i%2==0):
        lst.append(i)
    else:
        lst.append('Invalid')
            
#print(lst)

new_lst = [i if(i%2==0) else 'Invalid' for i in range(10)]  #List Comprehension [work in example-4]
print(new_lst)