# sum of natural number using recursion
def sum_nat(n):
    if n<=1:
        return n
    else:
        return sum_nat(n-1)+n
n = int(input("Enter the range to get the sum of natural number: "))
for i in range(n+1):
    sum = sum_nat(i)
print(sum)
