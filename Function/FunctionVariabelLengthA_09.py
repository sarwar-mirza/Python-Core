# Variable length Argument
''' Variable length argument is an argument that can accept any number of values,
    The variable length argument is written with * Symbol.
    it stores all the value in a tuple.
'''

def show(*num):                       #[koita argument asbe ta user jane na thokon * symbol deye call korthe hobe]
    z = num[0] + num[1] + num[2]      # Index sho bole dite hobe 
    print("Addition : ", z)

show(5,2,4)