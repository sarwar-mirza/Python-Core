# Global Keyword 

i = 0                      #Difine Golobal variable
def myfun():
    global i              #Global keyword
    while(i<5):
        print(i)
        i+=1
myfun()

print("Global :",i)     # Global Increment in last value [ex- first global variabel i = 0, increment i = 5]
        