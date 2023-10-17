# Dictionary Comprehension
'''
#Example-1
dict1 = {}
for n in range(10):
    dict1[n]= n*2            #dict1[n] = key & n*2 = value
#print(dict1)

new_dict = {n:n*2 for n in range(10) } #Dictionary Comprehension[ex-1]
print(new_dict)'''

'''
#Example-2
dict1 = {}
for n in range(10):
    if n%2==0:
        if n%3==0:
            dict1[n] = n*2
#print(dict1)

new_dict = {n:n*2 for n in range(10) if n%2==0 if n%3==0}  #Dictionary Comprehension[ex-2]
print(new_dict)'''


#Example-3
dict1 = {}
for n in range(10):
    if n%2==0:
        dict1[n]= n*2
    else:
        dict1[n]="Invalid"
#print(dict1)

new_dict = {n:n*2 if n%2==0 else 'Invalid' for n in range(10)}
print(new_dict)
