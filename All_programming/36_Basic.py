# Convert Decimal

num = int(input("Enter a number: "))
i =1
bin = 0
while num>0:
    print(num%2,end='')
    bin = bin+(num%2)*i
    i*=10 
    num=num//2
print()    
print(bin)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Convert Decimal to Binary using Recursion
def dec_to_bin(n):
    if n>0:
        dec_to_bin(n//2)
        # return n%2
        print(n%2,end='')
n = int(input("Enter a number:"))
dec_to_bin(n)
