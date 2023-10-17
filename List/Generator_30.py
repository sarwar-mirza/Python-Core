# Generator 
'''Yield Statement -> Yield statement returns the elements from a generator function into a 
                      generator object'''
# next()--> next(Generator_Object)

def show(a,b):
    while a<=b:
        yield a              #Applying yield and return A function
        a+=1

result = show(1,5)

print(next(result))          # next() function use 
print(next(result))
''' print result 1, 2 tar por for loop use korleo dui(2) r por theke count korbe
    karon last print thke for loop kaj kora suru korbe'''
for i in result:           
    print(i)
    