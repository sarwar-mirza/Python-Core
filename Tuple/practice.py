# Getting tuple from user input very complicated but as programmer logic can do 
a = (10,20,30,(40,50))
n = len(a)
i = 0
while i<n:
    if type(a[i]) is tuple:
        j = 0
        while j<len(a[i]):
            print(i,j,"=",a[i][j])
            j+=1
        i+=1
    else:
        print(i,"=",a[i])
        i+=1