# Nested List

a = [10,20,30,[40,50]]                 #1st Nested list
print("Before Modification A :",a)
a[1]= 44
a[3][0]= 77
print("After Modification A :", a)
print()

b = [140,150]                            #2nd Nested list
a = [101,102,103,b]
print("A :",a)
print("B :",b)
print()
print("Before Modification A :",a)
a[1]= 120
a[3][0]= 200
print("After Modification A :", a)
print()

a = [[210,220,230],                           #3rd Nested list
     [240,250,260]]

print("Before Modification A :",a)
a[0][1]= 40
a[1][2]= 77
print("After Modification Row/Column A :", a)
print()

