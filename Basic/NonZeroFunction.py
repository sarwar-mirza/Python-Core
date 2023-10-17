# nonzero()---> [zero hole tar index dekabe na ar nonzero gulor index dekabe]

from numpy import *
a = array([100,200,0,400,0,600])

result= nonzero(a)                 # total index 6 kinthu print korece 4 index (jegulo zeor se gulo bhad dice)
print(result)