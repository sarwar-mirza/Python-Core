# Comparing array using numpy -> >,<,<=,>=,==,!=

from numpy import *

a = array([100,120,103,110])
b = array([100,130,10,110])

c = a==b
d = a<b
e = a>=b
print(c)
print(d)
print(e)