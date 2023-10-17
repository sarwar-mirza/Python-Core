# where() Syntex-> where(condition, expression1, expression2)

from numpy import *
a = array([101, 12, 200,45,500])
b = array([100, 10, 300,55,50])

c = where(a>b,a,b)
print(c)