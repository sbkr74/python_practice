# Calculation based on user choice.
# simple calculator

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("\nChoose desired operations:")
choice = int(input("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\nChoose options: "))

result = 0

if choice == 1:
    result = num1+num2
    print("Result:",result)
elif choice == 2:
    result = num1-num2
    print("Result:",result)
elif choice == 3:
    result = num1*num2
    print("Result:",result)
elif choice == 4:
    if num2>0:
        result = num1/num2
        print("Result:",result)
    else:
        print(f"not defined as {num1} divided by {num2}.")
else:
    print("Invalid choice \nChoose from given")


# upcoming taking inputs in loop and perform operations on them.