num = int(input('Enter The Number : '))

while(num<=3):
    print("Outer Loop", num)
    num+=1
    j = 1
    while(j<=3):
        print('Inner Loop', j)
        j+=1
else:
    print('While condition False so else part executed')
print('Rest of the code')