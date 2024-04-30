# Find numbers divisible by another number.
# using anonymous function
'''
there will be list having some random numbers.
I WILL TAKE INPUT FROM USER UPTO WHICH THEY WANT TO CHECK i.e another number
then we will store and print it
'''

'''
Example:
[12,13,39,30,55,65]
2 = 12,30
3 = 12,39,30
4 = 12
5 = 30,55,65
6 = 12,30
7 = none
8 = none 
.
.
.
'''
usr_list = [12,13,39,30,55,65]
# for item in usr_list:
#     for i in range(2,13):
#         if(item%i==0):
#             print(i,"=",item)

for i in range(2,14):
    div = []
    for item in usr_list:
        if(item%i==0):
            # print(i,"=",item)
            div.append(item)
    if div == []:
        continue
    print(i,"=",div)
