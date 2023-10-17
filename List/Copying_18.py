# Copying list -->New_list_name = list_name.copy()

''' When we copy a list a separate copy of all the elements is stored in another list.
Both the list are independent. 
Modification in A will not affect B and vice versa'''

a = [10,20,30,40,50]
b = a.copy()              #Applying copy() Method 
print("A : ",a)
print("B : ",b)
print()


print("Modifaying A List")
a[1]= 77
print("A : ",a)                 # Modifying A list
print("B : ",b)                 # Modification in A will not affect B 
print()

print("Modifaying B List")
b[0]= 55
print("A : ",a)                 # Modification in B will not affect a
print("B : ",b)                 # Modifying B list  
print()