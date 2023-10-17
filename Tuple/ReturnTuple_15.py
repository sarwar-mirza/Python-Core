# Passing and Returning Tuple

def show(t):                      # Create Function and Receiving Perameter/Argumnent
    print(t)
    print(type(t))                # Check This Type
    for i in t:
        print(i)
    return t


tup = (10,20.5,-87,'Sarwar')
New_tup = show(tup)              # Calling Function and Passing Argument 
print(New_tup)
print(type(New_tup))
print()