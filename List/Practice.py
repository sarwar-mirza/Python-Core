# Higher order function
a = [33,40,60,50,75,20,80,60,90]
b = [1,2,3,4,5,6,7,8,9]
result = list(filter(lambda n: n>=60, a))      #filter(function_name, iterable)
print(result)
print(type(result))
print()
result = list(map(lambda m,n: m+n, a,b))
print(result)
from functools import *
b = [1,2,3,4,5,6,7,8,9]
result = reduce(lambda m,n: m+n, b)
print(result)


'''my_lst = []
temp_lst = []
n = int(input('Elements: '))
for i in range(n):
    m = int(input("Element inner: "))
    for j in range(m):
        temp_lst.append(input("Element: "))
    my_lst.append(temp_lst)
    temp_lst= []
print(my_lst)'''




'''from numpy import *
n = int(input("Enter number of elements: "))
doc = zeros(n)
m = len(doc)
for i in range(m):
    x = int(input("Element: "))
    doc[i] = x
print(doc)'''

'''from numpy import *
row = int(input("Enter Number Of Rows: "))
column = int(input("Enter Number Of Columns: "))
doc = zeros((row,column))
n = len(doc)
for i in range(n):
    for j in range(len(doc[i])):
        x = int(input("Enter Element: "))
        doc[i][j]= x
    print()
for i in range(len(doc)):
    for j in range(len(doc[i])):
        print(i,j,"=",doc[i][j])
    print()'''
'''
banknote = float(input())
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(banknote/100)))
remaining = (banknote%100)
print("{} nota(s) de R$ 50.00".format(int(remaining/50)))
remaining = (remaining%50)
print("{} nota(s) de R$ 20.00".format(int(remaining/20)))
remaining = (remaining%20)
print("{} nota(s) de R$ 10.00".format(int(remaining/10)))
remaining = (remaining%10)
print("{} nota(s) de R$ 5.00".format(int(remaining/5)))
remaining = (remaining%5)
print("{} nota(s) de R$ 2.00".format(int(remaining/2)))
remaining = (remaining%2)
print("MOEDAS:")
moedas_re = remaining
print("{} moeda(s) de R$ 1.00".format(int(moedas_re/1)))
rem_mod = (moedas_re%1)
print("{} moeda(s) de R$ 0.50".format(int(rem_mod/0.50)))
rem_mod = (rem_mod%0.50)
print("{} moeda(s) de R$ 0.25".format(int(rem_mod/0.25)))
rem_mod = (rem_mod%0.25)
print("{} moeda(s) de R$ 0.10".format(int(rem_mod/0.10)))
rem_mod = (rem_mod%0.10)
print("{} moeda(s) de R$ 0.05".format(int(rem_mod/0.05)))
rem_mod = (rem_mod%0.05)
print("{} moeda(s) de R$ 0.01".format(int(rem_mod/0.01)))'''




