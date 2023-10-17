''' Type Of Adding = Two type add in set type 
           (i). Single Adding
           (ii). Multiple Adding
    Single--> We can add a new element to set using add() method
             Syntex= set_name.add(new_element)

    Multiple--> We can add multiple elements to set using update() method
            Syntex= set_name.update(new_elements)
'''

print("Single adding ")
a = {10,20,'Sarwar', 40}
a.add('Python')
print("Single Add: ",a)
print(id(a))
print(type(a))
print()

print("************************")
print("Multiple Adding ")
b = {99,88,'mithu',77}
print("Before Adding : ",b)
x = [101,102,103]
b.update(x)
print("After Multiple Adding : ",b)