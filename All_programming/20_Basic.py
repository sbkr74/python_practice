# Armstrong Number
# 407 = (4*3)+(0*3)+(7*3)
num = int(input("Enter a number: "))
arm = 0
while num != 0:
    x = num%10
    arm = x**3+arm
    num = num//10
print(arm)