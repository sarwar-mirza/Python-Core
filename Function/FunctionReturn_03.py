# Return Statement Single Value

def add(y):
    x = 10
    z = x + y
    return z         #Using Return statement
sum = add(20)
print(sum)
print()


# Return Statement More than value

def add_sub(b):
    a = 20 
    c = a + b 
    d = a - b
    return c,d           # Using more than value return


sum, sub = add_sub(40)             
print("Addition :",sum)
print("Subtraction :",sub)