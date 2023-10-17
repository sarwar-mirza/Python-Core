# pop() --> list_name.pop()         [last element delete]
# pop(n)--> list_name.pop(Position_number) [specific position delete and return Element]

a = [10,20,12.4,-45,'Md Golam Sarwar']
print("Before POP : ",a)

a.pop()                                #Applaying pop() Method
print("After POP : ",a)

print()

a = [10,20,12.4,-45,'Md Golam Sarwar']
print("Bofore POP():", a)

n = a.pop(2)             #Applying pop(n) Method[Specific Position Nnumber Delete]
print("After POP() :",a)

print()
print("Romove/Deleteing Element : ",n)          #Returning Position Number 