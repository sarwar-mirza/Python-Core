#Higher Order Function-1
#filter()--> filter(Function_Name,Iterable)
''' It returns those elements of sequence.
For which function is TRUE'''

'''
def high_marks(n):                        # Function define with Receving Argument
    if n>=60:
        return True

a = [10,50,60,80,90,5,45,65]
result = list(filter(high_marks, a))      #Applying filter() function use and convert to list
print(result)
'''


a = [10,50,60,80,90,6,45,65]
result = list(filter(lambda n: (n>=60),a))
print(result)