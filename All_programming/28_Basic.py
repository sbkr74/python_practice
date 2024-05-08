# LCM
# 54 = 2,3,3,3
#24 = 2,2,2,3
# L.C.M = 2*3*3*3*2*2 = 216
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
# temp = num1
# temp2 = num2
# k=2
# l=2
# k1=[]
# l1=[]
# for i in range(2,temp):
#     if(temp%k==0):
#         temp = temp//k
#         k1.append(k)
#     else:
#         k=k+1
# for j in range(2,temp2):
#     if(temp2%l==0):
#         temp2 = temp2//l
#         l1.append(l)
#     else:
#         l=l+1
# print(k1)
# print(l1)

# still need to complete
##############################################################
if(num1>num2):
    larger = num1
else:
    larger = num2
y =1
for x in range(1,larger):
    if (num1%x==0) and (num2%x==0):
        y = y*x
        num1=num1//x
        num2=num2//x
    else:
        continue
print(y*num1*num2)