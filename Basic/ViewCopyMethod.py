#view() Method
#copy()Method

from numpy import *
a = array([10,20,30,40,50])
b = a.view()                  #Using view() Method - memory loction aladha dekabe

print('a', a)
print('b', b)
print()
print('a ', id(a))
print('b ', id(b))
print()
print('Modifay After veiw method')
a[1]=222
b[3]=444
print('Modifay :', a)
print('Modifay :', b)


print('After copy() Method ')
a = array([10,20,30,40,50])
b = a.copy()                  #Using copy() Method - a er maan change korele b er maan change hobe na

print('a', a)
print('b', b)
print()
print('a ', id(a))
print('b ', id(b))
print()
print('Modifay After veiw method')
a[1]=202
b[3]=404
print('Modifay :', a)
print('Modifay :', b)