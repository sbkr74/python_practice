#fibonacci Series
# 0 1 1 2 3 5 8 13
num1 = 0
num2 = 1
upto = int(input("Enter the range for fibonacci: "))
print(num1,num2,end=" ")
for _ in range(upto):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")
    
    # print(num1)