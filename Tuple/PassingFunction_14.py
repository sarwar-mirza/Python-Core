# Passing Tuple To Function

def show(t):                   #Create Function and receiving Perameter/Argument
    print(t)
    print(type(t))             # Check Type
    for i in t:                # Accessing For Loop
        print(i)

tup = (10,20,5,-50,'Sarwar')
show(tup)                         # Calling Function and Passing Arugument