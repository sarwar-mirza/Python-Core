#any() Function-->  [je kono ekta TRUE hole TRUE result dibe]
#all() Function-->  [sob TRUE holei TRUE result dibe abar sob FALSE hole FALSE result dibe]

from numpy import *
a = array([100,200,300,400,500])
b = array([100,20,300,40,500])

c = a == b
print(c)
print()

print(any(c))      #Using any() Function
print()
print(all(c))      #Using all() Function