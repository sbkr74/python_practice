# All prime in intervals
num = int(input("Enter a number: "))
set1 = set()
set2 = set()
for ele in range(2,num):
    set1.add(ele)

for i in range (2,num):
    for j in range(2,i):
        if(i%j==0):
            set2.add(i)
# print(set1)
# print(set2)
# set3 =set1.remove(set2)
set3 = set1 - set2
print(set3)