# Examples of loops

# 1 to 10
for i in range(1,11):
    print(i,end=" ")

print()

# 10 to 1
for i in range(10,0,-1):
    print(i,end=" ")

print()

# 1 to n
n = int(input("Enter number: "))
for i in range(1,n+1):
    print(i,end=" ")

print()

# n to 1
n = int(input("Enter number: "))
for i in range(n,0,-1):
    print(i,end=" ")

print()

# m to n
m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))
for i in range(m,n+1):
    print(i,end=" ")
