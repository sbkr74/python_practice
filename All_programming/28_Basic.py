# LCM
# 54 = 2,3,3,3
#24 = 2,2,2,3
# L.C.M = 2*3*3*3*2*2 = 216
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
temp = num1
temp2 = num2
k=2
l=2
k1=[]
l1=[]
for i in range(2,temp):
    if(temp%k==0):
        temp = temp//k
        k1.append(k)
    else:
        k=k+1
for j in range(2,temp2):
    if(temp2%l==0):
        temp2 = temp2//l
        l1.append(l)
    else:
        l=l+1
print(k1)
print(l1)

# print(k1)