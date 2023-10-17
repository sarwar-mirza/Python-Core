# Pass a Function as Parameter 
def disp(sh):
    print( "Display Function " + sh())

def show():
    return "Show Function"

disp(show)