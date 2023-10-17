# Syntex --> for variable in sequence

start = int(input('Starting Point Initialization : '))
stop = int(input('stoping Point : '))
stepsize = int(input('Increement Point : '))

a = range(start, stop, stepsize)
for i in a:                                            #Using for loop
    print(i)