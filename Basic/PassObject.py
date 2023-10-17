# pass or call by object reference

def myfun(lst):
    print("Inside Function Before append :", lst, id(lst))
    lst.append(40)
    print("Inside Function After append :",lst, id(lst))        #append howar por bhinno memeory allocation hoy nai 


lst = [10,20,30]
print("Before Calling Function : ",lst, id(lst))
myfun(lst)
print("After Calling Function : ",lst, id(lst))