#Getting Input From USer

stu = {}
n = int(input("Enter Number Of Elements : "))

for i in range(n):
    k = input("Enter Keys : ")
    v = input("Enter Values : ")
    stu.update({k:v})
print()

for i in stu:
    print(i,' =',stu[i])
