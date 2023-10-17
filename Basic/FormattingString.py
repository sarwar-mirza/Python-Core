# Replacement Field = {index/key:[fill][align][sign][#][0][width][,][.precission]type}

print("{} {}".format(10,20))
print("{num1} {num2}".format(num1=30,num2=40))
print("Hello My Name Is {}".format('Sarwar Mithu'))
print("{} {}".format(330,'mithu'))
print("{:d} {:d}".format(10,20))                       #type--> convert (strig to integer)
print("{:5d} ".format(15))                        # [width]->5 ta box thori kore dibe
print("{num:05d} ".format(num=25))                #[0]->Padding korce
print("{num:+5d} ".format(num=25))                #[sign]-> addition,subtraction(+,-, space)
print("{num:<5d} ".format(num=25))                #[align]->right shift, left shift(<,>,^,=)
print("{num:*^5d} ".format(num=25))
print("{num:*<5d} ".format(num=25))               #[fill]-> je kono symbol deoa jabe($,@,*,&)
print("{num:8.2f} ".format(num=25.342))           #[.precission]-> dhosomik por koi digit nibe 
print("{num:,}".format(num=1234567432))           #[,]-> Thousand por comma dibe

name = "Abu Taher"
age = 65
print("My name is {} and my age is {}".format(name,age))

data = {"abir":3000,"liza":6000}
print("{0[abir]:d} {0[liza]:d}".format(data))
print("{abir} {liza}".format(**data))



print("*********** f-string Format*****************")

#Syntex -> {index/key/name:[fill][align][sign][#][0][width][,][.precission]type}


name = "f-string"
a = "f/F"
print(f"Hello I am {name} and i start from  {age}")

num = 15
print(f"{num}")
print(f"{num:d}")
print(f"{num:5d}")
print(f"{num:05d}")
print(f"{num:+5d}")
print(f"{num:<5d}")
print(f"{num:*<5d}")
print(f"{num:^5d}")
print(f"{num:*^5d}")

price = 15.2347654
print(f"{price:8.3f}")       #float 

name = 'Sarwar'
print(f"{name:12s}")       #string

a = 50
b = 3
print(f"{a/b:.2%}")

x = 'Sarwar Mithu'
print(f"{x.upper()}")     #function()