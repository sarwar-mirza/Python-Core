num1 = int(input('Enter The First Number : '))
num2 = int(input('Enter The Second Number : '))


if(num1>=num2):
    print('\"Correct\" You Have Entered Greater Than Equal : ', num1)
    num3 = int(input('Enter The Thrid Number : '))
    num4 = int(input('Enter The Forth Number : '))
    if(num3<=num4):
        print('\'Correct\'', num3 ,'Your Have Entered less than equal :', num4)
    else:
        print('Oops batter than next time')
else:
    print('\"Wrong\" You Have Entered : ', num2)

print("Rest Of The Code")