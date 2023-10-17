# Deleting Dictionary Item

stu = {101:'Lima', 102:'Liza',103:'Abir',104:'Python'}
print("Before Deletion ")
print(stu)
print(id(stu))
print()

del stu[103]                        #Specific item delete Only
print("After Deletion ")
print(stu)
print(id(stu))
print()


#del stu                            #Puro dictionary delete hoye jabe 