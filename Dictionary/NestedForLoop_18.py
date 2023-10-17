#Accessing Neseted Dictionary Using For Loop
#Create empty Nested dict dict_name = {'dict_1':{}, 'dict_2': {}}
                                        
a = {'Course':'Python', 'Fees': 45000, 1:{'Course':'Java', 'Fees':30000}}

for i in a:
    if type(a[i]) is dict:
        for j in a[i]:
            print(j,'= ',a[i][j])
    
    else:
        print(i,' = ',a[i])