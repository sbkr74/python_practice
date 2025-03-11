# sum of odd numbers upto input

num = int(input("Enter a number: "))
sum = 0
for i in range(1,num+1):
    if i%2==1:
        print(i,end=" ")
        sum+=i
print("\nSum of above odds =",sum)
    