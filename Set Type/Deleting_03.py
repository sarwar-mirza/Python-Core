''' We can delete element using remove() OR discard() methods.
   --> remove() method raise an error if element doesn't exists while discard() method remains unchanged
        Syntex --> set_Name.remove(element)
        Syntex --> set_Name.discard(element)
'''

a = {10,20,'Sarwar',40}
print("Before Deleting Set A: ",a)
print(id(a))
print(type(a))
print()

a.remove('Sarwar')                     #element doesn't exists ERROR IN CODE 
#a.discard('mithu')                    #element doesn't exists no ERROR IN CODE  
print("After Deleting Set A: ",a)
print(id(a))
print(type(a))
print()