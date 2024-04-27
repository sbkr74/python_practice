# Power of 2 using Anonymous Function
term = int(input("Enter the range upto which you need exponential:"))
result = list(map(lambda x: 2 **x,range(term)))
print("power of 2 upto",term)
for i in range(term):
    print("2 power",i,"is",result[i])
# ==============================================================================
# term = int(input("Enter the range upto which you need exponential:"))
# n = int(input("Enter number whose exponential you want:"))
# result = list(map(lambda x: n **x,range(term)))
# print("power of 2 upto",term)
# for i in range(term):
#     print(n,"power",i,"is",result[i])