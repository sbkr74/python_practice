# perfect square
print("Program to check for perfect square.")
num = int(input("Enter a number: "))
digit = 1
flag = 0
while digit<=num//2:
    if num/digit==digit:
        print(num,"is perfect square of",digit)
        flag = 1
        break
    else:
        digit+=1

if flag == 0:
    print(num,"is not perfect square.")

# Using module
# Approach -1
import math
print("\nApproach-1:")

num_sqrt = int(math.sqrt(num))
if num == num_sqrt*num_sqrt:
    print(num,"is perfect square of",num_sqrt)
else:
    print(num,"is not perfect square.")

# Approach -2
# searching for optimization that can be done.