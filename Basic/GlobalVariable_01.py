# Local Variable and Global Variable 

a = 30                #Define Global Variable any palace in Use 
def add():
    x = 10
    print("Local Variable : ",x)    # Calling Local Variable
    print("Global Variable : ",a)   # calling Global Variable

add()
print("Global Variable : ",a)          # calling Global Variable