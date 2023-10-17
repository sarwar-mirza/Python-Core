# keyword variable length

def show(**num):                           #keyword r shomoy ** Symbole deye call korthe hobe
    z = num['a'] + num['b'] + num['c']
    print("Addition : ", z)

show(a=5,b=2,c=4)