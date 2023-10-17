# Aliasing List
#Aliasing means giving another name to existing object. it doesn't mean copying.
#Modification in A will affect B and vice versa 

a = [10,20,30,40,50,]
b = a                    #Aliasing List
print("A :",a)
print("B :",b)
print()

print("Modifaying A list ")
a[2] = 45
print("A :",a)                 # Modification in A will affect B 
print("B : ",b)                # Modification in A will affect B 
print()

print("Modifaying B list ")
b[0] = 110
print("A :",a)               # Modification in B will affect A 
print("B : ",b)              # Modification in B will affect A
print()