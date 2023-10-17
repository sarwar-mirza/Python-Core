# Higher Order Function -3
# reduce()--> reduce(Function_Name, Sequence)
''' from functools import reduce '''

from functools import *
a = [10,20,30,40,50]

result = reduce(lambda m,n: m+n, a)     # Applaying reduce() Function, Useing lambbda Function
print(result)
print(type(result))