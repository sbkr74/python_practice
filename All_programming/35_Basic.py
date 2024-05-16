# Factorial using recursion
def fact(n):
    if n<=1:
        return n
    else:
        return fact(n-1)*n
num = int(input("Enter a number to find factorial: "))
print("factorial of {} is {}.".format(num,fact(num)))
