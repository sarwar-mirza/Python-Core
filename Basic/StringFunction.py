# String Function

name = "Sarwar Mithu"
u = name.upper()               #calling upper() Function
print('Capital letter : ',u)
print('Lower :',u.lower())     #calling lower() Function

a = 'SARWAR MITHU'
b = 'sarwar mithu'

c = 's1r3w6A8'
d = 'SarwarMithu'
e = '163410020'
f = ' '
print('capital to small convert : ',a.swapcase())
print('Small to Capital convert : ',b.swapcase())

print('Check this format In upper : ',a.isupper())
print('Check this format In upper : ',b.isupper())

print('Check this format In Lower : ',b.islower())
print('Check this format In Lower : ',a.islower())

print('Check this format In Alpha : ',d.isalpha())
print('Check this format In Alpha : ',c.isalpha())

print('Check this format Is Digit : ',e.isdigit())
print('Check this format Is Digit : ',d.isdigit())

print('Check this format any Numeric/alpha/Combine : ',c.isalnum())
print('Check this format any Numeric/alpha/Combine : ',d.isalnum())
print('Check this format any Numeric/alpha/Combine : ',e.isalnum())

print('Check this format is Space : ',f.isspace())
print('Check this format is Space : ',a.isspace())

g = "   Sarwar mithu    "
print("Remove Left side Space :", g.lstrip())
print("Remove Right side Space :", g.rstrip())
print("Remove Both Of Side Space :",g.strip())

n = "hello my name is sarwar mithu"
n1 = "Hello My Name Is Sarwar Mithu"
print('First letter always Capital : ', n.title())
print('Check this format In title : ',n.istitle())
print('Check this format In title : ',n1.istitle())


z = "JavaProgramming"
q = "Java"
w = "Python"
print("With Variable Repalace String : ", z.replace(q,w)) 
print("Without Variable Repalace String : ", z.replace('Java','Python')) 


sentence = "Hello World! How are you"
date = "11-07-2023"
print("Separat to multiple String :", sentence.split())  # Splitting by default space separator
print("Separat to multiple String :", date.split('-'))                 # Splitting at the hyphen separator

my_list = ["apple", "banana", "orange"]
result = ",_ ".join(my_list)
print(result)

print(" Check Spicefied word in your string :",sentence.startswith('Hello'))    #startswith() Function calling
print(" Check Spicefied word in your string :",sentence.startswith('How'))
print(" Check Spicefied word in your string :",sentence.endswith('you'))        #endswith() Function calling
print(" Check Spicefied word in your string :",sentence.endswith('are'))
