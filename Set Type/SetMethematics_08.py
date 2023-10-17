# Some importent set methods 
a = {'Rahul','Raj','Sonam','Rani'}
b = {'Sarwar','Rahul','Rani','Python','Java'}

print('A : ',a)
print('B : ',b)

x = a.intersection(b)   #Exists both In Set a or b
print(x)
print()

x = a.union(b)          # All Elements 
print(x)
print()

x = a.difference(b)     #  a & b maje je gulo mil nei sei gulo dekabe sodhu a elements ke gurutto debe
print(x)
print()

x = a.issubset(b)       # same hole TRUE ar same na hole FALSE dekabe
print(x)
print()

x = a.issuperset(b)   # Orginal set elements jai thak kinthu Specified set ektao bashi thakle FALSE dekabe
print(x)
print()