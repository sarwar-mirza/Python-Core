#Returning Function 

def show(d):
    print(d)
    print(id(d))
    print(type(d))
    for i in d:
        print(i,d[i])
    return d

dic = {101:'Liza',102:'Lima',103:'Sarwar'}
new_dic = show(dic)
print(new_dic)
print(id(new_dic))
print(type(new_dic))