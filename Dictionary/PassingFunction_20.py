#Passing Dictionary to Function

def show(d):
    print(d)
    print(id(d))
    print(type(d))
    for i in d:
        print(i,d[i])

dic = {101:"Liza",102:"Lima",103:"Sarwar"}
show(dic)