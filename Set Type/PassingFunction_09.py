# Passing set to Function

def show(s):
    print(s)
    print(id(s))
    print(type(s))
    for i in s:
        print(i)
    print()

st = {10,20.5,-50,'Sarwar'}
show(st)