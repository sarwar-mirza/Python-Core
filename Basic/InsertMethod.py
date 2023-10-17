# insert() Method 
#Syntex--> array_name.insert(Position_number,New_Element)
from array import *
st = array('i', [102,103,104,105])

n = len(st)
i=0
while (i<n):
    print('index',i,'= ', st[i])
    i+=1
print('After Insert() method ')

st.insert(0,101)
st.insert(2,109)
n = len(st)
j = 0
while(j<n):
    print('insert Index ', j,'=', st[j])
    j+=1