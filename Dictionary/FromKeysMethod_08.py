'''This method is used to create a new dictionary with the specified keyw and values.
   Syntex -> dict.fromkeys(keys, value)
'''

key = (101,102,103)    # keys a Tuple 
value = 'python'
d = dict.fromkeys(key, value)
print(d)
print()
for i in d:
    print(i,'= ',d[i])