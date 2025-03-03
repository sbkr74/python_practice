# perfect square
print("Program to check for perfect square.")
x = int(input("Enter a number: "))
i = 2
flag = 0
while i<x//2:
    if x//i==i:
        print(x,"is perfect square of",i)
        flag = 1
        break
    else:
        i+=1
        
if flag == 0:
    print(x,"is not perfect square.")