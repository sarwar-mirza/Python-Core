# Function Decoratoor
def decor1(num):
    def inner():
        a = num()
        x = a * 5
        return x
    return inner

def decor(num):
    def inner():
        add = num() + 5
        return add
    return inner

@decor                   #[@ Symbol dete hoy call korar jonno]   ex- num = decor(decor1((num)))
@decor1
def num():
    return 10

print(num())