# Returning set from Function

def show(s):
    print(s)
    print(id(s))
    print(type(s))
    for i in s:
        print(i)
    return s

st = {10,20.5,-50,'Sarwar'}
New_st = show(st)
print(New_st)
print(id(New_st))
print()