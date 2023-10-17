# Passing and returning list

def show(l):                   #define Function
    print(l)
    print(type(l))             #Check type
    for i in l:               
        print(i)
    return l                   #Returning list

lst = [10,20,30,'Sarwar']      #declear list
New_list=show(lst)             #Calling Function and Passing Argument
print(New_list)
print(type(New_list))