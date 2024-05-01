#HCF or GCD
# 54 and 24 is 6
num1 = int(input("first numbeer:"))
num2 = int(input("second numbeer:"))
k=[]
for i in range(1,num1):
    if(num1%i==0):
        k.append(i)
l=[]
for j in range(1,num2):
    if(num2%j==0):
        l.append(j)
commons = set(k) & set(l)
print("HCF of",num1,"and",num2,"is",max(commons))

