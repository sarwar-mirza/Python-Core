# Higer Order Function -2
# map() --> map(Function_Name, Iterable)

a =[10,20,30,40]      # Each elements 2 add

result = list(map(lambda n: (n+3), a))   # Applaying map() Function and Convert to list, Useing lambbda Function
print(result)