# Nested Function 
def disp():
    def show():
        print("Show Function ")
    print("Disp Function ")
    show()

disp()




# With Argument Passing to Parameter

def disp(st):
    def show():
        return "Sarwar Mithu "
    result = show() + st + " In Python Code"
    return result
a = disp("Programmer")
print(a)
