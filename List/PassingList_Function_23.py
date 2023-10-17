# Passing List To Function


def show(l):                 #Define Function  [perameter (l=lst)]
    print(l)
    print(type(l))
    for i in l:
        print(i)

lst = [10,20,30,'Sarwar']
show(lst)                    # Calling Function and Passing Argument 