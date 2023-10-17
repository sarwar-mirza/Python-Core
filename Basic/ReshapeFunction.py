#reshape() Function 

from numpy import * 
a = array([1,2,3,4,5,6,7,8,9,10,11,12])
b = reshape(a,(2,6))                    #Applying 1D to 2D arry Convert
print(a)
print(b)
print()

c = reshape(a,(3,2,2))                #Applying 1D to 3D arry convert
print(c)