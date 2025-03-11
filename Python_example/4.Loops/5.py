# generate a series having square of every +ve integer upto input

print("Generate a sequence of square numbers upto n.")
while True:
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Input only accept digits.")

for i in range(1,num+1):
    print(i*i,end=" ")

print("\nAnother approach")
# Using Math module
from math import pow

for i in range(1,num+1):
    print(int(pow(i,2)),end=" ")

# Note: Using pow() we can print cubic as well as quadratic or power of n.
# just use pow(num,n)
# where num will integers of numbers and n will power of that integer.