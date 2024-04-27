# list of armstrong number
num1 = int(input("Enter starting range: "))
num2 = int(input("Enter ending range: "))

for i in range(num1,num2):
    arm =0
    k=i
    while i != 0:
        x=i%10
        arm=x**3+arm
        i//=10
    # print(arm)
    if(arm==k):
        print(k)
