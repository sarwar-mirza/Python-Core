# Access Nested Using For Loop

a = {1:{'Course':'Python Language','Fees':30000},
     2:{'Course':'Java','Fees':20000}
    }

n = len(a)
for i in a:
    for j in a[i]:
        print(j,'= ',a[i][j])
    