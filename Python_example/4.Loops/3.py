# Table example
import math

while True:
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Only digits are allowed.Try again!")

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")