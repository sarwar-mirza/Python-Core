# Global Function 

a = 50            # Define global variable

def show():
    a = 10                         # define local variable
    print("Local Variable : ",a)

    x = globals()['a']              # Calling Global function -> globals()[]    
    print("X :",x)

    x = 30                          # global function na likhle ta local variable hisabe dore nei
    print("X :",x)

show()
print("Global Variabale : ",a)