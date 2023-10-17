# Recursion Function 

i = 0                            #global varibale 
def myfun():
    global i                     #global keyword
    i=i+1
    print("My Function :",i)
    myfun()                       # Function called in function it is recursion function
myfun()