#Nested Function
# Function Return Another Function
def disp():
    def show():
        return "Show Function"
    print("Disp Function")
    return show                            # return Show() Function

r_sh = disp()
print(r_sh())                              #Calling Show() Function




#Function Return Another Function With Argument Passig another Function

def disp(sh):
    print("Disp Function")
    return sh

def show():
    return "Show Function"

r_sh = disp(show)
print(r_sh())